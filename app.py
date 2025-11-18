from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from google import genai
from google.genai import types
import time
import os
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
import logging

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = "uploads"
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file size
ALLOWED_EXTENSIONS = {'pdf', 'txt', 'doc', 'docx'}

# Initialize Gemini client
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

client = genai.Client(api_key=api_key)

FILE_SEARCH_STORE = client.file_search_stores.create()
print("Using File Store:", FILE_SEARCH_STORE.name)

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file_to_store(file_path):
    """Upload file to Gemini file search store with error handling"""
    try:
        upload_op = client.file_search_stores.upload_to_file_search_store(
            file_search_store_name=FILE_SEARCH_STORE.name,
            file=file_path
        )
        while not upload_op.done:
            time.sleep(2)
            upload_op = client.operations.get(upload_op.name)
        logger.info(f"Successfully uploaded file: {file_path}")
        return True
    except Exception as e:
        logger.error(f"Error uploading file {file_path}: {str(e)}")
        raise

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_files():
    """Handle file uploads with validation and error handling"""
    try:
        if "files" not in request.files:
            return jsonify({"error": "No files provided"}), 400

        files = request.files.getlist("files")
        if not files or files[0].filename == '':
            return jsonify({"error": "No files selected"}), 400

        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        uploaded_files = []
        errors = []

        for file in files:
            try:
                # Validate file
                if not allowed_file(file.filename):
                    errors.append(f"{file.filename}: File type not allowed. Allowed: {', '.join(ALLOWED_EXTENSIONS)}")
                    continue

                # Secure the filename
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

                # Save and upload file
                file.save(file_path)
                upload_file_to_store(file_path)
                uploaded_files.append(filename)
                logger.info(f"File uploaded successfully: {filename}")

            except Exception as e:
                errors.append(f"{file.filename}: {str(e)}")
                logger.error(f"Error processing file {file.filename}: {str(e)}")

        if not uploaded_files and errors:
            return jsonify({"error": "No files were uploaded. " + " ".join(errors)}), 400

        message = f"Successfully uploaded {len(uploaded_files)} file(s)"
        if errors:
            message += f". {len(errors)} file(s) failed: " + " ".join(errors)

        return jsonify({"message": message, "uploaded": uploaded_files}), 200

    except Exception as e:
        logger.error(f"Unexpected error in /upload: {str(e)}")
        return jsonify({"error": "Server error during upload"}), 500

@app.route("/ask", methods=["POST"])
def ask():
    """Handle question queries with error handling and validation"""
    try:
        # Validate request
        if not request.json:
            return jsonify({"error": "Request must be JSON"}), 400

        user_question = request.json.get("question", "").strip()
        if not user_question:
            return jsonify({"error": "Question cannot be empty"}), 400

        if len(user_question) > 5000:
            return jsonify({"error": "Question too long (max 5000 characters)"}), 400

        logger.info(f"Processing question: {user_question[:100]}...")

        # Generate content with Gemini
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=user_question,
            config=types.GenerateContentConfig(
                tools=[types.Tool(
                    file_search=types.FileSearch(
                        file_search_store_names=[FILE_SEARCH_STORE.name]
                    )
                )]
            )
        )

        # Extract answer
        if not response.candidates:
            return jsonify({"error": "No response generated"}), 500

        answer = response.text or "No answer generated"

        # Extract sources safely
        sources = []
        try:
            grounding = response.candidates[0].grounding_metadata
            if grounding and hasattr(grounding, 'grounding_chunks'):
                sources = list({c.retrieved_context.title for c in grounding.grounding_chunks if c.retrieved_context})
        except (AttributeError, IndexError, TypeError):
            logger.warning("Could not extract grounding metadata")

        logger.info(f"Question processed successfully with {len(sources)} sources")
        return jsonify({"answer": answer, "sources": sources}), 200

    except Exception as e:
        logger.error(f"Error in /ask: {str(e)}")
        return jsonify({"error": "Failed to process question"}), 500

@app.errorhandler(413)
def request_entity_too_large(error):
    """Handle file size limit exceeded"""
    return jsonify({"error": "File too large (max 50MB)"}), 413

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f"Internal server error: {str(error)}")
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    # Ensure upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Run on LAN (use --cert and --key for HTTPS in production)
    app.run(host="0.0.0.0", port=5000, debug=False)
