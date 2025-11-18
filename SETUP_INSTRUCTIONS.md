# Setup Instructions for Document Chatbot

## Quick Start (5 minutes)

### Step 1: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure API Key

1. Get your Google Gemini API key from https://ai.google.dev/
2. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
3. Edit `.env` and replace `your_api_key_here` with your actual API key:
   ```
   GOOGLE_API_KEY=sk-...your_actual_key...
   ```

### Step 4: Run the Application

```bash
python app.py
```

Open your browser and visit: `http://localhost:5000`

## What's New (Professional Improvements)

### Security Enhancements
✅ API key moved to environment variables (.env file)
✅ XSS protection with proper input sanitization
✅ CORS enabled for cross-origin requests
✅ Input validation on all endpoints
✅ File type and size restrictions

### Code Quality
✅ Comprehensive error handling
✅ Logging system for debugging
✅ Input length validation (5000 char limit)
✅ Secure filename handling
✅ Safe HTML escaping in frontend

### User Interface
✅ Modern, responsive design
✅ Loading spinners for feedback
✅ Alert notifications (success/error/info)
✅ Keyboard support (Enter to send)
✅ Better visual hierarchy
✅ Accessibility improvements

### Validation & Limits
✅ File upload: max 50MB per file
✅ Allowed formats: PDF, TXT, DOC, DOCX
✅ Question length: max 5000 characters
✅ Empty input checking
✅ File selection validation

### Documentation
✅ README.md with full documentation
✅ Inline code comments
✅ Requirements.txt with versions
✅ .gitignore for safety
✅ .env.example template

## File Structure

```
AI_chatbot_Sugarcane/
├── app.py                    # Main Flask application (UPDATED)
├── templates/
│   └── index.html           # Web UI (COMPLETELY REDESIGNED)
├── uploads/                 # User uploaded files
├── app.ipynb               # Original notebook
├── requirements.txt        # NEW - Python dependencies
├── .env.example            # NEW - Environment template
├── .env                    # NEW - Your actual config (NOT in git)
├── .gitignore             # NEW - Prevents secrets from being committed
├── README.md              # NEW - Complete documentation
└── SETUP_INSTRUCTIONS.md  # This file
```

## Important Notes

### Security ⚠️
- **NEVER** commit `.env` to git
- **NEVER** share your API key
- The `.env` file is already in `.gitignore` to protect you
- Always use environment variables for secrets

### Before Running
1. Ensure you have Python 3.8+
2. Create and activate virtual environment
3. Install dependencies from requirements.txt
4. Set up `.env` with your API key
5. Make sure port 5000 is available

### Troubleshooting

**"GOOGLE_API_KEY environment variable is not set"**
- Solution: Make sure you created `.env` file with your API key

**"ModuleNotFoundError: No module named 'flask'"**
- Solution: Run `pip install -r requirements.txt`

**Port 5000 already in use**
- Solution: Change port in app.py line 182 or kill the process using port 5000

**Upload fails with "File type not allowed"**
- Only PDF, TXT, DOC, DOCX are supported
- Files must be smaller than 50MB

## Production Deployment

For production use:

1. Set `FLASK_DEBUG=False` in `.env`
2. Use a production WSGI server:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```
3. Set up HTTPS with proper certificates
4. Use a reverse proxy (nginx, Apache)
5. Enable proper logging and monitoring
6. Use environment-specific configuration

## Testing the App

After starting the application:

1. Visit `http://localhost:5000`
2. Upload a test PDF or TXT file
3. Type a question about the document
4. Press Enter or click Send
5. You should see the AI response with sources

## Support

If you encounter issues:
1. Check the console output for error messages
2. Verify your API key is correct
3. Ensure files are in supported formats
4. Check file sizes (max 50MB)
5. Review the README.md for detailed information

---

**Your app is now professional-grade and ready for use!** 🚀
