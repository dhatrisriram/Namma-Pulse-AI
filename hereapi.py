import pandas as pd
import requests
import time

# Constants
API_KEY = "aMdlpzV__Fi_dsa66B8zZEa1jmfg21jBTXsTy-Yjl0Q"
INPUT_FILE = "All-time Table-Bangalore-Wards.csv"
OUTPUT_FILE = "C:/Users/Dhatri P Sriram/Desktop/Dhatri/Projects/Predictive Surge/Updated_Bangalore_Wards.csv"
BASE_URL = "https://geocode.search.hereapi.com/v1/geocode"

# Load the dataset
ride_data = pd.read_csv(INPUT_FILE)

# Check if lat/lon already exist, if not add them
if 'latitude' not in ride_data.columns:
    ride_data['latitude'] = None
if 'longitude' not in ride_data.columns:
    ride_data['longitude'] = None

# Fetch coordinates for each ward
def get_coordinates(ward_name):
    params = {
        'q': f'{ward_name}, Bangalore, India',
        'apiKey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['items']:
            position = data['items'][0]['position']
            return position['lat'], position['lng']
    return None, None

# Iterate over each row to get coordinates
for idx, row in ride_data.iterrows():
    if pd.isna(row['latitude']) or pd.isna(row['longitude']):
        lat, lng = get_coordinates(row['Ward'])
        ride_data.at[idx, 'latitude'] = lat
        ride_data.at[idx, 'longitude'] = lng
        print(f"Ward: {row['Ward']}, Lat: {lat}, Lng: {lng}")
        time.sleep(1)  # Avoid hitting rate limits

# Save the updated file
try:
    ride_data.to_csv(OUTPUT_FILE, index=False)
    print(f"Updated dataset saved to {OUTPUT_FILE}")
except Exception as e:
    print("Error:", e)
