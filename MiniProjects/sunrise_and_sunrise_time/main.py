import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()["iss_position"]
# latitude = data["latitude"]
# longitude = data["longitude"]
#
# location = (latitude, longitude)
# print(location)
my_location_parameter ={
    "lat": 28.682280,
    "lng": 77.023700,
    "formatted":0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=my_location_parameter)
data = response.json()["results"]
sunrise = data["sunset"].split("T")[1].split(":")
# sunri =  sunrise[1].split(":")

print(sunrise)