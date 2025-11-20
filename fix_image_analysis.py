import re

# Read the file
with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find and replace the problematic section
old_pattern = r'''        # Ensure file search store is available
        store = ensure_file_search_store\(\)

        # Use Gemini Vision API for image analysis
        response = client\.models\.generate_content\(
            model='gemini-2\.0-flash',
            contents=\[
                types\.Content\(
                    parts=\[
                        types\.Part\(text=analysis_prompt\),
                        types\.Part\(inline_data=types\.Blob\(
                            mime_type=image_file\.content_type or 'image/jpeg',
                            data=image_bytes
                        \)\)
                    \]
                \)
            \],
            config=types\.GenerateContentConfig\(
                tools=\[types\.Tool\(
                    file_search=types\.FileSearch\(
                        file_search_store_names=\[store\.name\]
                    \)
                \)\]
            \)
        \)'''

new_code = '''        # Use Gemini Vision API for image analysis (no file_search needed for images)
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=[
                types.Content(
                    parts=[
                        types.Part(text=analysis_prompt),
                        types.Part(inline_data=types.Blob(
                            mime_type=image_file.content_type or 'image/jpeg',
                            data=image_bytes
                        ))
                    ]
                )
            ]
        )'''

# Replace
content = re.sub(old_pattern, new_code, content, flags=re.DOTALL)

# Write back
with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed image analysis - removed file_search tools")
