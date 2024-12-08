import requests
import os

FLIC_TOKEN = "your_flic_token"

async def upload_videos(file_path):
    try:
        # Step 1: Get pre-signed upload URL
        headers = {"Flic-Token": FLIC_TOKEN, "Content-Type": "application/json"}
        response = requests.get("https://api.socialverseapp.com/posts/generate-upload-url", headers=headers)
        response.raise_for_status()
        upload_url = response.json()["url"]
        video_hash = response.json()["hash"]
        
        # Step 2: Upload video
        with open(file_path, "rb") as f:
            upload_response = requests.put(upload_url, data=f)
            upload_response.raise_for_status()
        
        # Step 3: Create Post
        body = {
            "title": os.path.basename(file_path),
            "hash": video_hash,
            "is_available_in_public_feed": False,
            "category_id": 1
        }
        post_response = requests.post("https://api.socialverseapp.com/posts", json=body, headers=headers)
        post_response.raise_for_status()

        # Step 4: Delete local file after successful upload
        os.remove(file_path)
        print(f"Uploaded and deleted: {file_path}")
    except Exception as e:
        print(f"Error uploading {file_path}: {e}")
