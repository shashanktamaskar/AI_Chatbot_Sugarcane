# Document Chatbot

A professional web application that allows users to upload documents and ask questions about them using Google's Gemini AI with file search capabilities.

## Features

- Upload multiple documents (PDF, TXT, DOC, DOCX)
- Ask questions about your documents
- Get AI-powered responses with source citations
- Beautiful, responsive user interface
- Secure API handling with environment variables
- Input validation and error handling
- File size limits and type restrictions
- XSS protection

## Prerequisites

- Python 3.8 or higher
- Google Gemini API key (get it at https://ai.google.dev/)

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd AI_chatbot_Sugarcane
```

### 2. Create a virtual environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` to `.env` and add your Google Gemini API key:

```bash
cp .env.example .env
```

Edit `.env` and add your API key:
```
GOOGLE_API_KEY=your_actual_api_key_here
```

**Important:** Never commit the `.env` file to version control. It contains sensitive information.

## Running the Application

### Development Mode

```bash
python app.py
```

The application will be available at `http://localhost:5000`

### Production Mode

For production deployment, consider:

1. Setting `FLASK_DEBUG=False` in `.env`
2. Using a production WSGI server like Gunicorn:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

3. Using HTTPS with proper certificates
4. Setting up proper logging and monitoring

## Usage

### Upload Documents

1. Click "Choose Files" and select one or more documents
2. Click "Upload Files"
3. Wait for the upload to complete

### Ask Questions

1. Type your question in the input field
2. Press Enter or click "Send"
3. The AI will respond with an answer and source documents

## File Specifications

- **Supported formats:** PDF, TXT, DOC, DOCX
- **Max file size:** 50MB per file
- **Max question length:** 5000 characters

## API Endpoints

### POST /upload
Upload documents to the chatbot

**Request:**
```
Content-Type: multipart/form-data
files: [file1, file2, ...]
```

**Response:**
```json
{
  "message": "Successfully uploaded 2 file(s)",
  "uploaded": ["file1.pdf", "file2.pdf"]
}
```

### POST /ask
Ask a question about uploaded documents

**Request:**
```json
{
  "question": "What is mentioned about sugarcane cultivation?"
}
```

**Response:**
```json
{
  "answer": "Based on the documents...",
  "sources": ["document1.pdf", "document2.pdf"]
}
```

## Security Features

- API keys stored in environment variables
- XSS protection through input sanitization
- File type validation
- File size limits
- Input length validation
- CORS protection
- Error messages don't expose sensitive information

## Troubleshooting

### API Key Not Set
```
ValueError: GOOGLE_API_KEY environment variable is not set
```
Solution: Ensure `.env` file exists and contains `GOOGLE_API_KEY=your_key`

### Upload Fails
- Check file size (max 50MB)
- Verify file format is supported
- Check server logs for detailed error messages

### Questions Not Returning Answers
- Ensure documents have been uploaded successfully
- Check that documents contain searchable text
- Verify API key has proper permissions

## Development

### Code Structure
```
.
├── app.py                 # Flask application and routes
├── templates/
│   └── index.html        # Web interface
├── uploads/              # User-uploaded files
├── .env                  # Environment variables (not in version control)
├── .env.example          # Environment template
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

This project is licensed under the MIT License - see LICENSE file for details.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review the application logs
3. Check Google Gemini API documentation

## Future Enhancements

- User authentication and session management
- Chat history persistence
- Document management interface
- Advanced search filters
- Rate limiting
- Batch processing
- Document preview
- Multi-language support

---

**Note:** Keep your Google API key secure. Never share it or commit it to version control.
