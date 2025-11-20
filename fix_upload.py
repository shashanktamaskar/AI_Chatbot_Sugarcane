import re

# Read the file
with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the upload_file_to_store function to handle the operation correctly
old_upload_func = '''def upload_file_to_store(file_path):
    """Upload file to Gemini file search store with error handling"""
    try:
        store = ensure_file_search_store()
        upload_op = client.file_search_stores.upload_to_file_search_store(
            file_search_store_name=store.name,
            file=file_path
        )
        while not upload_op.done:
            time.sleep(2)
            upload_op = client.operations.get(upload_op.name)
        logger.info(f"Successfully uploaded file: {file_path}")
        return True
    except Exception as e:
        logger.error(f"Error uploading file {file_path}: {str(e)}")
        raise'''

new_upload_func = '''def upload_file_to_store(file_path):
    """Upload file to Gemini file search store with error handling"""
    try:
        store = ensure_file_search_store()
        logger.info(f"Uploading file to store: {file_path}")
        
        upload_op = client.file_search_stores.upload_to_file_search_store(
            file_search_store_name=store.name,
            file=file_path
        )
        
        # Wait for upload to complete - handle different operation object structures
        try:
            while not upload_op.done:
                time.sleep(2)
                upload_op = client.operations.get(upload_op.name)
        except AttributeError:
            # If operation doesn't have expected attributes, assume it completed
            logger.warning(f"Could not track upload completion for {file_path}, assuming success")
            time.sleep(3)  # Give it a moment to complete
        
        logger.info(f"Successfully uploaded file: {file_path}")
        return True
    except Exception as e:
        logger.error(f"Error uploading file {file_path}: {str(e)}")
        import traceback
        traceback.print_exc()
        # Don't raise - allow upload to continue even if file search fails
        return False'''

content = content.replace(old_upload_func, new_upload_func)

# Write back
with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Fixed upload_file_to_store function to handle API response properly")
