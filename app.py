import streamlit as st
import folium
from streamlit_folium import folium_static
from twilio.rest import Client
from folium.plugins import HeatMap
import os

# Clear any Streamlit cache to prevent old code from appearing
st.legacy_caching.clear_cache()

# Set up Streamlit UI
st.title("🚖 Ride-Hailing Surge Prediction Dashboard")

# Map configuration
st.subheader("📍 Surge Zones Map")

# Bengaluru Coordinates
city_lat, city_lon = 12.9716, 77.5946
m = folium.Map(location=[city_lat, city_lon], zoom_start=12)

# Example Surge Zones (replace with real-time predicted data)
surge_zones = [
    [12.9611, 77.6015],  # MG Road
    [12.9755, 77.6055],  # Indiranagar
    [12.9279, 77.6271],  # Koramangala
]

# Add Heatmap to show Surge Areas
HeatMap(surge_zones, radius=25).add_to(m)

# Add Markers for each surge location
for lat, lon in surge_zones:
    folium.Marker([lat, lon], popup="🚦 High Demand Here!", icon=folium.Icon(color="red")).add_to(m)

# Display Map
folium_static(m)

# Twilio SMS Alert
st.subheader("📲 Send Surge Alert to All Drivers")

alert_button = st.button("🚀 Send Surge Alert")

# Function to get all verified phone numbers from your Twilio account
def get_verified_twilio_numbers():
    # Retrieve Twilio credentials from environment variables
    TWILIO_SID = os.getenv('TWILIO_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')

    if not all([TWILIO_SID, TWILIO_AUTH_TOKEN]):
        st.error("⚠️ Twilio credentials are missing. Please set them in your environment.")
        return []

    try:
        # Initialize Twilio client
        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

        # Get all verified phone numbers associated with the Twilio account
        phone_numbers = []

        # List verified caller IDs (this includes numbers you have added and verified for messaging)
        verified_numbers = client.incoming_phone_numbers.list(voice_enabled=False)  # Can use 'voice_enabled=False' to fetch messaging numbers

        for number in verified_numbers:
            phone_numbers.append(number.phone_number)

        return phone_numbers
    except Exception as e:
        st.error(f"⚠️ Error fetching verified Twilio phone numbers: {e}")
        return []

# Function to send SMS to all verified Twilio numbers
def send_bulk_alert(phone_numbers, message):
    # Retrieve Twilio credentials from environment variables
    TWILIO_PHONE = os.getenv('TWILIO_PHONE')  # Your Twilio phone number

    if not TWILIO_PHONE:
        st.error("⚠️ Twilio phone number is missing. Please set it in your environment.")
        return

    try:
        # Initialize Twilio client
        client = Client(os.getenv('TWILIO_SID'), os.getenv('TWILIO_AUTH_TOKEN'))

        # Send message to all verified phone numbers
        for number in phone_numbers:
            client.messages.create(
                body=message,
                from_=TWILIO_PHONE,
                to=number
            )

        st.success(f"✅ Alert sent to {len(phone_numbers)} verified numbers.")
    except Exception as e:
        st.error(f"⚠️ Error sending SMS: {e}")

# Real-time notification sending
if alert_button:
    # Get all verified phone numbers from Twilio account
    phone_numbers = get_verified_twilio_numbers()

    if phone_numbers:
        # Send the surge alert message to all verified numbers
        message = "🚖 Surge Alert: High ride demand in your area. Please move towards the hotspot!"
        send_bulk_alert(phone_numbers, message)
    else:
        st.warning("⚠️ No verified phone numbers found in your Twilio account.")
