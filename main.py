import os
import json
import datetime
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# Configuration
OUTPLAYED_FOLDER = r"C:\Users\YOUR_USERNAME\Videos\Overwolf\Outplayed" # Users will need to change this
HISTORY_FILE = "uploaded_videos.json"
CLIENT_SECRET_FILE = "client_secret.json"
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def get_authenticated_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('youtube', 'v3', credentials=creds)

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    return []

def save_history(history):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f)

def format_title(filename):
    # Example: Valorant_05-10-2025_22-13-59-550.mp4
    name_without_ext = os.path.splitext(filename)[0]
    parts = name_without_ext.split('_')
    
    if len(parts) >= 3:
        game_name = parts[0]
        date_part = parts[1]
        time_part = parts[2].replace('-', ':')
        return f"{game_name} Gameplay - {date_part} {time_part}"
    return name_without_ext

def upload_video(youtube, file_path, title):
    print(f"Uploading: {title}...")
    request_body = {
        "snippet": {
            "categoryId": "20", # Gaming category
            "title": title,
            "description": "Recorded with Outplayed. Auto-uploaded."
        },
        "status": {
            "privacyStatus": "private" # Set to 'public' or 'unlisted' if preferred
        }
    }
    
    media_file = MediaFileUpload(file_path, chunksize=-1, resumable=True)
    request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media_file
    )
    response = request.execute()
    print(f"Upload Successful! Video ID: {response['id']}")

def main():
    print("Starting Outplayed Auto-Uploader...")
    youtube = get_authenticated_service()
    history = load_history()
    
    # Walk through the Outplayed directory and its subfolders
    for root, dirs, files in os.walk(OUTPLAYED_FOLDER):
        for file in files:
            if file.endswith(".mp4"):
                file_path = os.path.join(root, file)
                
                # Check if already uploaded
                if file_path not in history:
                    title = format_title(file)
                    try:
                        upload_video(youtube, file_path, title)
                        history.append(file_path)
                        save_history(history)
                    except Exception as e:
                        print(f"Failed to upload {file}: {e}")
                else:
                    print(f"Already uploaded: {file}")

if __name__ == "__main__":
    main()
