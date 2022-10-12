import requests
from twilio.rest import Client

API_KEY = "a12678c926d155fbc02579c07bf2484d"
account_sid = "ACa58f1ab954e8eec7979c39660d80b85e"
account_auth = "96b6db50d5beb6ea9ea527452b6d2214"
account_num = '+19036626873'

api_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
weather_parameters= {
    "lat" : "30.409916",
    "lon" : "103.475775",
    "exclude":"current,minutely,daily",
    "appid":API_KEY
}


response = requests.get(api_endpoint, params=weather_parameters)
response.raise_for_status()
hourly_data = response.json()["hourly"]
condition_code_data = [hourly_data[i]["weather"][0]["id"] for i in range (0,13)]

is_rain = False
for id in condition_code_data:
    if id <700:
        is_rain = True
if is_rain:
    client = Client(account_sid, account_auth)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring Umbrella",
        from_=account_num,
        to='+916202592138'

    )
    print(message.status)
