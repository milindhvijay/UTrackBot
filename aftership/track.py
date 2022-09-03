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

response = requests.get('https://api.aftership.com/v4/trackings', headers=headers, params=params)


#print(response.text)

#data = response.text
#parse_json = json.loads(data)

#slug=parse_json['data']['trackings'][0]['slug']
#print(slug)

data = response.json()
city = data['data']['trackings'][0]['checkpoints'][0]['city']

print(city)