# 🌾 Farmer-Focused Agricultural Advisory System - Setup Guide

## Overview

This application is a specialized chatbot designed for farmers, particularly those working with sugarcane cultivation. It provides expert agricultural advice in 6 Indian languages with voice input/output and crop disease identification capabilities.

## Features

### ✅ Multi-Language Support
- **English** - For urban and educated farmers
- **हिंदी (Hindi)** - Most widely spoken
- **मराठी (Marathi)** - Maharashtra sugarcane belt
- **தமிழ் (Tamil)** - Tamil Nadu farmers
- **తెలుగు (Telugu)** - Telangana & Andhra Pradesh
- **ಕನ್ನಡ (Kannada)** - Karnataka farmers

### ✅ Voice Input/Output
- **Voice Questions**: Click the microphone button to ask questions using your voice
- **Text-to-Speech**: Listen to answers in your selected language
- Works on mobile browsers (Chrome, Safari, Edge recommended)

### ✅ Crop Disease Identification
- Upload images of crop leaves, stems, or affected areas
- AI analyzes the image to identify diseases, pests, or health issues
- Provides treatment recommendations based on knowledge base
- Supports JPG, JPEG, PNG formats (max 10MB)

### ✅ Document-Based Knowledge
- Upload PDF, TXT, DOC, DOCX files about agriculture
- System searches through documents to answer questions
- Provides source references for answers

### ✅ Farmer-Friendly UI
- Large fonts (18px minimum) for easy reading
- High contrast colors for visibility in sunlight
- Large touch targets (56px) for easier tapping
- Mobile-first responsive design
- Simple, clear visual hierarchy

---

## Knowledge Base Setup

### Folder Structure

The `knowledge_base/` directory contains agricultural documents organized by category:

```
knowledge_base/
├── sugarcane/              # Sugarcane cultivation guides
│   ├── cultivation_guide_hindi.pdf
│   ├── sugarcane_varieties.pdf
│   └── seasonal_calendar.txt
├── pest_control/           # Pest management information
│   ├── common_pests_identification.pdf
│   ├── organic_solutions_hindi.pdf
│   └── pesticide_guide.txt
├── diseases/               # Disease identification & treatment
│   ├── sugarcane_diseases.pdf
│   ├── disease_management.txt
│   └── symptoms_guide.pdf
├── market_info/            # Market prices & trends
│   ├── current_prices.txt
│   ├── price_trends.pdf
│   └── mandi_info.txt
└── government_schemes/     # Government programs & subsidies
    ├── subsidies_2025.pdf
    ├── insurance_guide.txt
    └── kisan_credit_card.pdf
```

### Adding New Documents

#### Step 1: Prepare Your Documents

**Best Practices:**
- Use clear, descriptive filenames (e.g., `sugarcane_red_rot_disease.pdf`)
- Include language suffix for regional content (e.g., `_hindi.pdf`, `_marathi.pdf`)
- Optimize PDFs for text extraction (searchable PDFs, not scanned images)
- Keep file sizes reasonable (<10MB per document)
- Use clear section headers within documents

**Content Guidelines:**
- Write in simple, farmer-friendly language
- Include practical, actionable advice
- Add visual diagrams where possible
- Provide step-by-step instructions
- Include local context (Indian farming practices)

#### Step 2: Organize by Category

Place documents in the appropriate folder:

- **sugarcane/** - Cultivation techniques, varieties, planting schedules
- **pest_control/** - Pest identification, organic solutions, pesticides
- **diseases/** - Disease symptoms, treatment, prevention
- **market_info/** - Prices, trends, market access
- **government_schemes/** - Subsidies, insurance, loan programs

#### Step 3: Upload to System

**Method 1: Direct Upload (via Web Interface)**
1. Open the chatbot application
2. Go to "Upload Documents" section
3. Select your prepared files
4. Click "Upload Files"
5. Wait for confirmation message

**Method 2: Server Upload (for administrators)**
1. Copy files to the appropriate `knowledge_base/` subfolder
2. Restart the application or trigger document indexing
3. Files will be automatically processed

#### Step 4: Verify Upload

Test the new documents by asking relevant questions:
- "गन्ने में लाल सड़न रोग का इलाज क्या है?" (Hindi)
- "What are the symptoms of red rot disease in sugarcane?" (English)
- "சக்கரை வெள்ளை நோய் எப்படி கட்டுப்படுத்துவது?" (Tamil)

### Document Naming Conventions

Use this format for consistency:
```
[topic]_[subtopic]_[language].extension

Examples:
- sugarcane_irrigation_best_practices_hindi.pdf
- pest_control_organic_methods_marathi.txt
- government_kisan_credit_card_english.pdf
```

### Language-Specific Content

For multilingual support:
- Create separate documents for each language, OR
- Include multilingual sections within a single document
- Tag language clearly in filename
- Use Unicode encoding (UTF-8) for Indian languages

---

## Using the Application

### For Farmers

#### 1. Select Your Language
- Click the language dropdown at the top
- Choose your preferred language
- All responses will be in that language

#### 2. Upload Agricultural Documents (Optional)
- Click "Choose Files" under "Upload Documents"
- Select PDF, Word, or text files about farming
- Click "Upload Files"
- Wait for success message

#### 3. Identify Crop Diseases
- Click "Choose File" under "Crop Disease Identification"
- Take/upload a clear photo of affected crop part
- Click "Analyze Image"
- Review disease identification and treatment advice

#### 4. Ask Questions

**Text Input:**
- Type your question in the text box
- Press Enter or click Send button

**Voice Input:**
- Click the microphone 🎤 button
- Speak your question clearly
- Wait for text to appear
- Click Send

**Listen to Answers:**
- After receiving an answer, click "Listen to Answer" button
- Audio will play in your selected language
- Click "Stop" to pause

### Example Questions

**Sugarcane Cultivation:**
- "गन्ने की बुवाई का सबसे अच्छा समय क्या है?" (When to plant sugarcane?)
- "ऊस लागवडीसाठी किती पाणी लागते?" (Water requirements?)
- "கரும்பு விதைப்பு எப்போது செய்ய வேண்டும்?" (Planting time?)

**Pest Control:**
- "गन्ने में सफेद सुंडी का उपचार?" (White grub treatment?)
- "ಜೀರುಂಡೆ ನಿಯಂತ್ರಣ ಹೇಗೆ?" (Beetle control?)

**Government Schemes:**
- "किसान क्रेडिट कार्ड कैसे मिलेगा?" (How to get Kisan Credit Card?)
- "What subsidies are available for sugarcane farmers?"

---

## Content Maintenance

### Regular Updates

**Monthly Tasks:**
- Update market price information
- Add seasonal farming advice
- Review and update pest outbreak alerts

**Quarterly Tasks:**
- Add new government scheme announcements
- Update fertilizer recommendations
- Review and improve existing content

**Annual Tasks:**
- Update cultivation calendars
- Add new variety information
- Archive outdated content

### Quality Checklist

Before uploading new content, verify:
- [ ] Information is accurate and up-to-date
- [ ] Language is simple and farmer-friendly
- [ ] No jargon or technical terms (or explained if necessary)
- [ ] Practical and actionable advice
- [ ] Relevant to local farming conditions
- [ ] Properly formatted and readable
- [ ] Source is credible (government, research institution, expert)

---

## Technical Notes

### Supported File Formats

**Documents:**
- PDF (.pdf) - Preferred for guides and manuals
- Text (.txt) - Good for simple information
- Word (.doc, .docx) - Acceptable but convert to PDF when possible

**Images (for disease identification):**
- JPEG (.jpg, .jpeg) - Recommended
- PNG (.png) - Acceptable
- Max size: 10MB per image

### System Limitations

- Maximum file size: 50MB for documents, 10MB for images
- Text extraction quality depends on PDF quality
- Voice recognition requires internet connection
- Text-to-speech quality varies by browser and language

### Browser Compatibility

**Best Experience:**
- Chrome/Edge (Desktop & Mobile)
- Safari (iOS/macOS)
- Firefox (Desktop)

**Limited Features:**
- Voice input may not work on older browsers
- Text-to-speech may have limited language support

---

## Troubleshooting

### Common Issues

**Problem: Voice input not working**
- Solution: Use Chrome/Safari browser, grant microphone permissions

**Problem: Document upload fails**
- Solution: Check file size (<50MB), ensure supported format

**Problem: Poor image analysis**
- Solution: Upload clear, well-lit images; focus on affected areas

**Problem: Answer not relevant**
- Solution: Upload more specific documents about the topic

**Problem: Language not displaying correctly**
- Solution: Ensure browser supports Unicode/UTF-8 encoding

---

## Best Practices for Farmers

### Getting the Best Results

1. **Be Specific**: Instead of "pest problem", say "white spots on leaves"
2. **Use Voice Input**: Easier than typing on mobile
3. **Upload Clear Photos**: Good lighting, focused on problem area
4. **Ask Follow-up Questions**: Get detailed explanations
5. **Save Important Answers**: Screenshot or note down advice

### Privacy & Data

- Uploaded documents are stored securely
- Questions and images are processed but not shared
- No personal data is collected without consent

---

## Support & Feedback

For technical issues or suggestions:
- Check the main README.md file
- Contact system administrator
- Report issues through proper channels

---

## Future Enhancements (Planned)

- [ ] Weather-based alerts and recommendations
- [ ] Offline mode for areas with poor connectivity
- [ ] SMS-based question/answer for feature phones
- [ ] Integration with market price APIs
- [ ] Community forum for farmer discussions
- [ ] Video tutorials in regional languages

---

## Credits

**Developed for:** Indian sugarcane farmers
**Powered by:** Google Gemini AI
**Languages:** Hindi, Marathi, Tamil, Telugu, Kannada, English
**Focus:** Practical, actionable agricultural advice

---

**Version:** 1.0
**Last Updated:** 2025
**Maintained by:** Development Team

---

For deployment instructions and technical setup, see README.md
