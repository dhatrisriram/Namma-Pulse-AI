import requests
import json

API_KEY = HERE Maps API Key

# Define the API URL
url = f"https://router.hereapi.com/v8/routes?transportMode=car&origin=52.5309837,13.3845671&destination=52.5263797,13.3686127&return=summary&apikey={API_KEY}"

# Make the API request
response = requests.get(url)
data = response.json()

# Save response to a file
with open("data/route_response.json", "w") as file:
    json.dump(data, file, indent=4)

print("✅ API response saved to data/route_response.json")
