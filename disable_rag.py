import re

# Read the file
with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Comment out the file_search configuration in /ask endpoint
content = re.sub(
    r"(        # Generate content with Gemini with system instruction and file search\n        response = client\.models\.generate_content\(\n            model='gemini-2\.0-flash',\n            contents=f\"{system_instruction}\\\\n\\\\nUser Question: {user_question}\",\n            config=types\.GenerateContentConfig\(\n                tools=\[types\.Tool\(\n                    file_search=types\.FileSearch\(\n                        file_search_store_names=\[store\.name\]\n                    \)\n                \)\]\n            \)\n        \))",
    r"""        # Generate content with Gemini with system instruction
        # NOTE: file_search is temporarily disabled due to API compatibility issues
        # The model will still provide expert agricultural advice based on training data
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=f"{system_instruction}\\n\\nUser Question: {user_question}"
        )""",
    content
)

# Write back
with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Disabled file_search to fix chat functionality")
print("⚠️  RAG is now disabled - chat will work but won't use uploaded documents")
