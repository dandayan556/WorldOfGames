import requests
from requests.exceptions import InvalidURL

try:
    response = requests.get("httpswldjfnsdgf:dsf hdsfg")
except InvalidURL:
    print("invalid url was given")