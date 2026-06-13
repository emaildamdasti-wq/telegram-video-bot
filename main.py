import os
import requests

TOKEN = os.environ["TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = f"https://api.telegram.org/bot{TOKEN}/sendVideo"

with open("video.mp4", "rb") as video:
    requests.post(
        url,
        data={"chat_id": CHAT_ID},
        files={"video": video}
    )

print("Video sent successfully")
