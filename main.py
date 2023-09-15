import requests


api_key = "597526efbae0aca1aa4940817bff913c"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

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

i = 0
for hour in data_slice:
    weather_id = hour['weather'][0]['id']
    if weather_id < 900:
        weather_codes.append(weather_id)
        print(f"Hour {i}: Bring an umbrella")
    i += 1

print(weather_codes)
print(data['hourly'][0]['weather'][0]['id'])