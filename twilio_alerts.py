from twilio.rest import Client

# Twilio Credentials (Replace with your actual credentials)
account_sid = 'AC656574919143f32e9da4568584a72125'
auth_token = 'b19992a6b345045138b25e5c4aeafd11'
twilio_number = '+17856209301'  # Replace with your Twilio phone number

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Function to send SMS
def send_sms(to_number, message):
    client.messages.create(
        body=message,
        from_=twilio_number,
        to=to_number
    )

# Function to send WhatsApp message
def send_whatsapp(to_number, message):
    client.messages.create(
        body=message,
        from_='whatsapp:' + twilio_number,
        to='whatsapp:' + to_number
    )

# Example usage
if __name__ == "__main__":
    send_sms("+919876543210", "🚖 Surge alert: High demand in Zone A!")
    send_whatsapp("+919876543210", "🚖 Surge alert: High demand in Zone A!")
