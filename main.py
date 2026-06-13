import os
import time
import requests
import schedule


TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")


def send_video():
    url = f"https://api.telegram.org/bot{TOKEN}/sendVideo"

    files = {
        "video": open("video.mp4", "rb")
    }

    data = {
        "chat_id": CHAT_ID,
        "caption": "انگیزشی"
    }

    requests.post(url, files=files, data=data)


schedule.every().day.at("07:00").do(send_video)


while True:
    schedule.run_pending()
    time.sleep(30)