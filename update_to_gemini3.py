import re

# Read the file
with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all model references with gemini-3-pro-preview
content = content.replace("'gemini-2.5-flash'", "'gemini-3-pro-preview'")
content = content.replace('"gemini-2.5-flash"', '"gemini-3-pro-preview"')
content = content.replace("'gemini-2.0-flash'", "'gemini-3-pro-preview'")
content = content.replace('"gemini-2.0-flash"', '"gemini-3-pro-preview"')

# Write back
with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Updated model to gemini-3-pro-preview")
print("   This is the latest Gemini 3 model with enhanced capabilities")
