import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('AFTERSHIP_API_KEY')

headers = {
    'Content-Type': 'application/json',
    'as-api-key': API_KEY,
}

params = {
    'tracking_number': 'RR123456789CN',
}

response = requests.get(
    'https://api.aftership.com/v4/trackings', headers=headers, params=params)


data = response.json()
city = data['data']['trackings'][0]['checkpoints'][0]['city']

print(city)
