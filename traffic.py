import requests
import pandas as pd

# API Keys
HERE_API_KEY = 
PREDICTHQ_API_KEY = 
WEATHER_API_KEY = 

# Base URLs
HERE_BASE_URL = "https://geocode.search.hereapi.com/v1/geocode"
TRAFFIC_BASE_URL = "https://traffic.ls.hereapi.com/traffic/6.3/flow.json"
ROUTING_BASE_URL = "https://router.hereapi.com/v8/routes"
PREDICTHQ_BASE_URL = "https://api.predicthq.com/v1/events/"
WEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Fetch coordinates and geocoding details

def get_coordinates(ward_name):
    params = {'q': f'{ward_name}, Bangalore, India', 'apiKey': HERE_API_KEY}
    response = requests.get(HERE_BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['items']:
            item = data['items'][0]
            position = item['position']
            address = item.get('address', {})
            return position['lat'], position['lng'], address
    return None, None, {}

# Fetch traffic data from HereMaps Traffic API
def get_traffic(lat, lng):
    params = {'prox': f'{lat},{lng},500', 'apiKey': HERE_API_KEY}
    response = requests.get(TRAFFIC_BASE_URL, params=params)
    if response.status_code == 200:
        return response.json().get('RWS', [])
    return None

# Fetch routing data for travel time and distance
def get_routing_data(lat, lng, dest_lat, dest_lng):
    params = {
        'origin': f'{lat},{lng}',
        'destination': f'{dest_lat},{dest_lng}',
        'transportMode': 'car',
        'return': 'summary',
        'apiKey': HERE_API_KEY
    }
    response = requests.get(ROUTING_BASE_URL, params=params)
    if response.status_code == 200:
        routes = response.json().get('routes', [])
        if routes:
            summary = routes[0]['sections'][0]['summary']
            return summary['duration'], summary['length']
    return None, None

# Fetch events from PredictHQ API
def get_events(lat, lng):
    headers = {'Authorization': f'Bearer {PREDICTHQ_API_KEY}'}
    params = {'within': f'5km@{lat},{lng}', 'sort': 'start'}
    response = requests.get(PREDICTHQ_BASE_URL, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get('results', [])
    return []

# Fetch weather details from OpenWeatherMap API
def get_weather(lat, lng):
    params = {'lat': lat, 'lon': lng, 'appid': WEATHER_API_KEY, 'units': 'metric'}
    response = requests.get(WEATHER_BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    return None

# Load dataset
ride_data = pd.read_csv('Updated_Bangalore_Wards.csv')
ride_data['events'] = None
ride_data['weather'] = None
ride_data['traffic'] = None
ride_data['travel_time'] = None
ride_data['travel_distance'] = None
ride_data['geocoding_info'] = None

# Enrich dataset
for idx, row in ride_data.iterrows():
    lat, lng = row['latitude'], row['longitude']
    if pd.isna(lat) or pd.isna(lng):
        lat, lng, address = get_coordinates(row['Ward'])
        ride_data.at[idx, 'latitude'] = lat
        ride_data.at[idx, 'longitude'] = lng
        ride_data.at[idx, 'geocoding_info'] = str(address)

    events = get_events(lat, lng)
    weather = get_weather(lat, lng)
    traffic = get_traffic(lat, lng)
    travel_time, travel_distance = get_routing_data(lat, lng, 12.9716, 77.5946)  # MG Road as default destination

    ride_data.at[idx, 'events'] = str(events)
    ride_data.at[idx, 'weather'] = str(weather)
    ride_data.at[idx, 'traffic'] = str(traffic)
    ride_data.at[idx, 'travel_time'] = travel_time
    ride_data.at[idx, 'travel_distance'] = travel_distance
    print(f'Updated: {row["Ward"]} with Events, Weather, Traffic, and Routing Data.')

# Save enriched dataset
ride_data.to_csv('Updated_Bangalore_Wards - Copy.csv', index=False)
print('Dataset updated with event, weather, traffic, and routing data!')
