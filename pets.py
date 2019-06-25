import json
import os
import datetime
from dotenv import load_dotenv
import requests

load_dotenv()

TOKEN = os.environ.get("PETFINDER_ACCESS_TOKEN")
#API_KEY = os.environ.get('API_KEY')

request_url = "https://api.petfinder.com/v2/animals"

headers = {"Authorization": f"Bearer {TOKEN}"}

def get_response(postcode):
    request_url = f"https://api.petfinder.com/v2/animals"
    response = requests.get(request_url, headers=headers)
    parsed_response = json.loads(response.text)
    return parsed_response

def transform_response(parsed_response):
    location= parsed_response["animals"][0]["contact"]["address"]["postcode"]

#print(type(response)) #>
#print(response.status_code)
#pprint(response.text)


#print(parsed_response.keys())

#parsed_response["animals"][0]["contact"]["address"]["postcode"]



#breakpoint()
#exit()

#INPUTS

time_now = datetime.datetime.now() #> datetime.datetime(2019, 3, 3, 14, 44, 57, 139564)

print("Welcome to Get-A-Pet")
print("---------------------------------")
postcode = input ("Please input your zip code to find pets in your area: ")
parsed_response = get_response(postcode)

    

#OUTPUTS

formatted_time_now = time_now.strftime("%Y-%m-%d %H:%M:%S") #> '2019-03-03 14:45:27'


#DISPLAY RESULTS


print("Searching for pets in your area...")
print("---------------------------------")
print(f"REQUEST AT: {formatted_time_now}")
print("---------------------------------")
print(f"Pet Location: {postcode}")
print("---------------------------------")
print("Your future best friend: ")
print("---------------------------------")
print("Nearest adoption center: ")
print("---------------------------------")
print("Thank you for using Get-A-Pet!")
   