import re

# Read the file
with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the image analysis endpoint name
content = content.replace(
    '@app.route("/analyze_crop_image", methods=["POST"])',
    '@app.route("/analyze", methods=["POST"])'
)

# Also fix the parameter name from "image" to "file" to match frontend
content = content.replace(
    'if "image" not in request.files:',
    'if "file" not in request.files:'
)
content = content.replace(
    'image_file = request.files["image"]',
    'image_file = request.files["file"]'
)

# Fix the response key from "analysis" to "response"
content = content.replace(
    'return jsonify({"analysis": analysis}), 200',
    'return jsonify({"response": analysis}), 200'
)

# Write back
with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Fixed image analysis endpoint:")
print("   - Route: /analyze_crop_image → /analyze")
print("   - Input: 'image' → 'file'")
print("   - Output: 'analysis' → 'response'")
