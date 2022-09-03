import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('AFTERSHIP_API_KEY')

headers = {
    'Content-Type': 'application/json',
    'as-api-key': API_KEY,
}

response = requests.get(
    'https://api.aftership.com/v4/last_checkpoint/utxea845839f9l7lgyn6y028', headers=headers)

data = response.json()

city = data['data']['checkpoint']['city']
message = data['data']['checkpoint']['message']

print(city)
print(message)
