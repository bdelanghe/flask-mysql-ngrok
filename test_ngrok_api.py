#!/usr/bin/env python3
"""
Example script showing how to access the Flask app via ngrok with the bypass header.
This demonstrates programmatic access that skips the browser warning page.
"""

import requests

# Your ngrok domain
NGROK_URL = "https://uneloped-yen-overcontentiously.ngrok-free.dev"

# Headers to bypass the ngrok browser warning page
headers = {
    "ngrok-skip-browser-warning": "true"
}

def test_api():
    """Test accessing the Flask app via ngrok"""
    try:
        print(f"Testing connection to {NGROK_URL}...")
        response = requests.get(NGROK_URL, headers=headers, timeout=10)
        
        if response.status_code == 200:
            print("✅ Successfully connected!")
            print(f"Response status: {response.status_code}")
            print(f"Response length: {len(response.text)} bytes")
        else:
            print(f"⚠️  Got status code: {response.status_code}")
            print(f"Response: {response.text[:200]}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error connecting: {e}")
        print("\nMake sure:")
        print("1. Flask app is running (python app.py)")
        print("2. ngrok is running (devenv up)")
        print("3. The ngrok URL is correct")

if __name__ == "__main__":
    test_api()

