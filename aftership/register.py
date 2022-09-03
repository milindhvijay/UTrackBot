import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('AFTERSHIP_API_KEY')

headers = {
    'as-api-key': API_KEY,
}

json_data = {
    'tracking': {
        'tracking_number': 'RR123456789CN',
    },
}

response = requests.post(
    'https://api.aftership.com/v4/trackings', headers=headers, json=json_data)

# print(response.text)

data = response.json()

id = data['data']['tracking']['id']

print(id)
