import json
import os
from dotenv import load_dotenv
import requests

load_dotenv()

TOKEN = os.environ.get("PETFINDER_ACCESS_TOKEN")

request_url = "https://api.petfinder.com/v2/animals"

headers = {"Authorization": f"Bearer {TOKEN}"}

response = requests.get(request_url, headers=headers)
#print(type(response)) #>
#print(response.status_code)
#pprint(response.text)

#parsed_response = json.loads(response.text)
#print(parsed_response.keys())

key = os.environ.get('API_KEY')


#pf = Petfinder(key)

#cats = pf.breed_list('cat')
#print(cats)