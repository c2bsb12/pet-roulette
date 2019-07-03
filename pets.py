import json
import os
import datetime
from dotenv import load_dotenv
import requests
import random

load_dotenv()

TOKEN = os.environ.get("PETFINDER_ACCESS_TOKEN")
#API_KEY = os.environ.get('API_KEY')

request_url = "https://api.petfinder.com/v2/animals"
#request_url2 = "https://api.petfinder.com/v2/organizations"

headers = {"Authorization": f"Bearer {TOKEN}"}

def get_response(postcode):
    request_url = "https://api.petfinder.com/v2/animals"
    request_url2 = "https://api.petfinder.com/v2/organizations"
    response = requests.get(request_url, headers=headers, params={'location': postcode})
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

print("*** Welcome to Pet Roulette ***")
print("---------------------------------")
postcode = input ("Please input your zip code to find adoptable pets in your area: ")

parsed_response = get_response(postcode)


num_animals = len(parsed_response["animals"])
my_random_animal = parsed_response["animals"][random.randint(0, num_animals)]


#print("type: " + my_random_animal["type"])
#print("breed: " + my_random_animal["breeds"]["primary"])

#found_animal = None
#for animal in parsed_response["animals"]:
   # animal_postcode = animal["contact"]["address"]["postcode"]
   # print(animal_postcode)
   # if animal_postcode == postcode:
      #  found_animal = animal
      #  break
        
#print(found_animal)
    

#OUTPUTS

formatted_time_now = time_now.strftime("%Y-%m-%d %H:%M:%S") #> '2019-03-03 14:45:27'

pet_type = my_random_animal["type"]
pet_breed = my_random_animal["breeds"]["primary"]
pet_name = my_random_animal["name"]
pet_zip = my_random_animal["contact"]["address"]["postcode"]
find_pet = my_random_animal["url"]
#pet_photos = my_random_animal["photos"]["medium"]

options=pet_zip


#DISPLAY RESULTS

print("Searching for pets in your area...")
print("---------------------------------")
print(f"REQUEST AT: {formatted_time_now}")
print("---------------------------------")
print("Pet Location: "+ (pet_zip))
print("---------------------------------")
print("your future best friend: "+ (pet_name))
print("---------------------------------")
print("Pet type: "+ (pet_type))
print("---------------------------------")
print("Breed: "+ (pet_breed))
#print("---------------------------------")
#print("Pet picture: "+ str(pet_photos))
print("---------------------------------")
print("Find " +(pet_name)+ ":" +" "+ (find_pet))
print("---------------------------------")
print("Thank you for using Get-A-Pet!")
   