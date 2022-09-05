import os
import requests
from dotenv import load_dotenv
from aftership.register import register_func

load_dotenv()


API_KEY = os.getenv('AFTERSHIP_API_KEY')

id = register_func(tracking_id = '')


def last_checkpoint_func(message, city):
    headers = {
        'Content-Type': 'application/json',
        'as-api-key': API_KEY,
    }

    response = requests.get(
        'https://api.aftership.com/v4/last_checkpoint/%s' % id, headers=headers)

    last_checkpoint_data = response.json()

    message = last_checkpoint_data['data']['checkpoint']['message']
    city = last_checkpoint_data['data']['checkpoint']['city']

    return message, city


"""headers = {
    'Content-Type': 'application/json',
    'as-api-key': API_KEY,
}

response = requests.get(
    'https://api.aftership.com/v4/last_checkpoint/%s' % id, headers=headers)

last_checkpoint_data = response.json()

city = last_checkpoint_data['data']['checkpoint']['city']
message = last_checkpoint_data['data']['checkpoint']['message']


print(message)
print(city)"""
