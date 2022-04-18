'''CI J'''
import requests

url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url)
response.raise_for_status()

data = response.json()

#Get coordinates
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)
