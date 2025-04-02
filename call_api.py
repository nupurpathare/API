import requests
import json

# Define the API endpoint
API_URL = "http://127.0.0.1:5000/recommend"  # Change this if hosted elsewhere

# Take user input for mood
user_mood = input("Enter your mood (Calm, Relax, Focus, Anxious): ")

# Prepare the data payload
data = {"mood": user_mood}

# Send POST request to API
response = requests.post(API_URL, json=data)

# Check response
if response.status_code == 200:
    track = response.json().get("track", "No track found.")
    print(f"Recommended Meditation Track: {track}")
else:
    print(f"Error: {response.status_code}, {response.text}")
