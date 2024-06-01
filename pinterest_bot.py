import requests
from requests_oauthlib import OAuth1

# Replace these with your actual keys
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

# Set up OAuth1 authentication
auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Endpoint for uploading a pin
url = "https://api.pinterest.com/v1/pins/"

# Data for the pin
data = {
    "note": "Check out this photo!",
    "image_url": "http://example.com/photo.jpg",
    "board": "your_pinterest_board_id"
}

# Make the POST request to upload the pin
response = requests.post(url, auth=auth, data=data)

if response.status_code == 201:
    print("Photo uploaded successfully!")
else:
    print(f"Failed to upload photo: {response.content}")
