import re

# Read the file
with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all instances of gemini-2.0-flash with gemini-2.5-flash
content = content.replace("'gemini-2.0-flash'", "'gemini-2.5-flash'")
content = content.replace('"gemini-2.0-flash"', '"gemini-2.5-flash"')

# Write back
with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Updated model from gemini-2.0-flash to gemini-2.5-flash")
print("   This is the latest model with better file_search support")
