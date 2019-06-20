from petpy import Petfinder
import pandas
from dotenv import load_dotenv
import os
load_dotenv()

key = os.environ.get('API_KEY')
print(key)

pf = Petfinder(key)

cats = pf.breed_list('cat')
print(cats)