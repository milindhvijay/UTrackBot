import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('AFTERSHIP_API_KEY')


def register_func(tracking_id):
    headers = {
        'as-api-key': API_KEY,
    }

    json_data = {
        'tracking': {
            'tracking_number': "RR123456789CN",
        },
    }

    response = requests.post(
        'https://api.aftership.com/v4/trackings', headers=headers, json=json_data)

    register_data = response.json()

    tracking_id = register_data['data']['tracking']['id']

    return tracking_id