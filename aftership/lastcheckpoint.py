import os
import requests
from dotenv import load_dotenv
from register import tracking_id

load_dotenv()


API_KEY = os.getenv('AFTERSHIP_API_KEY')

id = tracking_id

headers = {
    'Content-Type': 'application/json',
    'as-api-key': API_KEY,
}

response = requests.get(
    'https://api.aftership.com/v4/last_checkpoint/%s' % id, headers=headers)

last_checkpoint_data = response.json()

city = last_checkpoint_data['data']['checkpoint']['city']
message = last_checkpoint_data['data']['checkpoint']['message']


print(message)
print(city)
