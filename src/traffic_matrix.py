import requests
import json

# 🔑 Replace with your HERE Maps API Key
API_KEY = "aMdlpzV__Fi_dsa66B8zZEa1jmfg21jBTXsTy-Yjl0Q"

# 📍 List of key locations (latitude, longitude)
locations = [
    (52.5309837, 13.3845671),  # Location A
    (52.5263797, 13.3686127),  # Location B
    (52.5105798, 13.3758591),  # Location C
]

# 🕒 Store travel times in a dictionary
travel_times = {}

for i, (lat1, lon1) in enumerate(locations):
    for j, (lat2, lon2) in enumerate(locations):
        if i != j:  # ❌ Avoid calculating the same location
            url = f"https://router.hereapi.com/v8/routes?transportMode=car&origin={lat1},{lon1}&destination={lat2},{lon2}&return=summary&apikey={API_KEY}"
            response = requests.get(url)
            data = response.json()
            
            # Extract travel time (in seconds)
            travel_time = data["routes"][0]["sections"][0]["summary"]["duration"]
            travel_times[f"{i}-{j}"] = travel_time

            print(f"Travel time from {i} to {j}: {travel_time} seconds")

# 💾 Save the travel time matrix as a JSON file
with open("data/traffic_matrix.json", "w") as file:
    json.dump(travel_times, file, indent=4)

print("\n✅ Traffic matrix saved to data/traffic_matrix.json")
