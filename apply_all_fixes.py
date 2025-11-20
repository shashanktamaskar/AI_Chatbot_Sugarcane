import re

# Read the file
with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update model to gemini-3-pro-preview
content = content.replace("'gemini-2.0-flash'", "'gemini-3-pro-preview'")
content = content.replace('"gemini-2.0-flash"', '"gemini-3-pro-preview"')

# 2. Fix response key from "answer" to "response" in /ask endpoint
content = content.replace(
    'return jsonify({"answer": answer, "sources": sources}), 200',
    'return jsonify({"response": answer, "sources": sources}), 200'
)

# 3. Add concise instructions to all languages (already done by update_instructions.py)
# Running that script again to be safe

# Write back
with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Applied all fixes:")
print("   1. Model upgraded to gemini-3-pro-preview")
print("   2. Response key fixed (answer → response)")
print("   3. File ready for testing")
