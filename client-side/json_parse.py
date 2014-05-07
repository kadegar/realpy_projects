import json

output=json.load(open('cars.json'))
print output["CARS"][0]["MODEL"]