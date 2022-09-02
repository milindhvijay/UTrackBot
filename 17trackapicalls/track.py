import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('17TRACK_API_KEY')

#Get Tracking Details - POST https://api.17track.net/track/v2/gettrackinfo

url = "https://api.17track.net/track/v2/gettrackinfo"

payload = [
    {
        "number": "RR123456789CN"
    }
]
headers = {
    "content-type": "application/json",
    "17token": "API_KEY"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)