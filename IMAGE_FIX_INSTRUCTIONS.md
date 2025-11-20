# Image Analysis Fix

## Problem
The image analysis feature is failing because it's trying to use `file_search` tools with vision analysis. File search is for document search, NOT for image analysis.

## Solution
Remove the `file_search` tools configuration from the `/analyze` endpoint. The Gemini vision model can analyze images directly without any additional tools.

## Changes Needed in app.py

### Line 234-308: Replace the analyze_crop_image function

**Remove these lines (276-299):**
```python
        # Ensure file search store is available
        store = ensure_file_search_store()

        # Use Gemini Vision API for image analysis
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
            ],
            config=types.GenerateContentConfig(
                tools=[types.Tool(
                    file_search=types.FileSearch(
                        file_search_store_names=[store.name]
                    )
                )]
            )
        )
```

**Replace with:**
```python
        # Use Gemini Vision API for image analysis (no tools needed)
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
        )
```

This removes the `config` parameter with `file_search` tools, allowing the vision model to analyze the image directly.
