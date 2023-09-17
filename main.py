import requests
import os
from twilio.rest import Client

api_key = os.environ.get("OWM_API_KEY")
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "AC82dd3d30de616f9259c8ceb228cdf0b9"
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": 37.323,
    "lon": -122.0323,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get(url=OWM_endpoint, params=parameters)
response.raise_for_status()
data = response.json()

weather_codes = []
data_slice = data['hourly'][:12]
will_rain = False
sunny = False

for hour in data_slice:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
    elif int(condition_code) == 800:
        sunny = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella ☔",
        from_='+18449983839',
        to='+14086104838',
    )
elif sunny:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to be a sunny day today. ☀️😎",
        from_='+18449983839',
        to='+14086104838',
    )

    print(message.status)

