import requests
import json
import os
import time
from PIL import Image
import io

BASE_URL = "http://localhost:5000"

def print_status(test_name, status, details=""):
    icon = "✅" if status == "PASS" else "❌"
    print(f"{icon} {test_name}: {status}")
    if details:
        print(f"   Details: {details}")

def test_health():
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            print_status("Health Check", "PASS", response.json())
            return True
        else:
            print_status("Health Check", "FAIL", f"Status {response.status_code}")
            return False
    except Exception as e:
        print_status("Health Check", "FAIL", str(e))
        return False

def test_chat():
    # Test English
    try:
        payload = {"question": "What is sugarcane?", "language": "english"}
        response = requests.post(f"{BASE_URL}/ask", json=payload)
        if response.status_code == 200 and "response" in response.json():
            print_status("Chat (English)", "PASS")
        else:
            print_status("Chat (English)", "FAIL", response.text)
    except Exception as e:
        print_status("Chat (English)", "FAIL", str(e))

    # Test Hindi
    try:
        payload = {"question": "गन्ना क्या है?", "language": "hindi"}
        response = requests.post(f"{BASE_URL}/ask", json=payload)
        if response.status_code == 200 and "response" in response.json():
            print_status("Chat (Hindi)", "PASS")
        else:
            print_status("Chat (Hindi)", "FAIL", response.text)
    except Exception as e:
        print_status("Chat (Hindi)", "FAIL", str(e))

def test_image_analysis():
    # Create a dummy image
    img = Image.new('RGB', (100, 100), color = 'green')
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='JPEG')
    img_byte_arr.seek(0)

    files = {'file': ('test_crop.jpg', img_byte_arr, 'image/jpeg')}
    data = {'language': 'english'}

    try:
        response = requests.post(f"{BASE_URL}/analyze", files=files, data=data)
        if response.status_code == 200 and "response" in response.json():
            print_status("Image Analysis", "PASS")
        else:
            print_status("Image Analysis", "FAIL", f"Status: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print_status("Image Analysis", "FAIL", str(e))

def test_file_upload():
    # Create a dummy text file
    files = {'files': ('test_doc.txt', 'This is a test document about sugarcane.', 'text/plain')}
    
    try:
        response = requests.post(f"{BASE_URL}/upload", files=files)
        if response.status_code == 200:
            print_status("File Upload", "PASS", response.json().get('message'))
        else:
            print_status("File Upload", "FAIL", response.text)
    except Exception as e:
        print_status("File Upload", "FAIL", str(e))

if __name__ == "__main__":
    print("⏳ Waiting for server to start...")
    time.sleep(5)  # Wait for server to initialize
    
    print("\n🚀 Starting Automated Tests...\n")
    
    if test_health():
        test_chat()
        test_image_analysis()
        test_file_upload()
    
    print("\n✨ Testing Complete.")
