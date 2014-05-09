import requests
import json

origin="San Francisco"
destination="Los Angeles"
sensor="false"
mode="walking"
APIkey="x"

base_url="https://maps.googleapis.com/maps/api/directions/json?"

url=base_url+"origin="+origin+"&destination="+destination+"&sensor=false"+"&mode="+mode+"&key="+APIkey

print url
directions=requests.get(url)

output=directions.json()

for route in output['routes']:
	for leg in route['legs']:
		for step in leg['steps']:
			print step['html_instructions']

