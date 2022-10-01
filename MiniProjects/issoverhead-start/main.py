import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "sachita.nand@yahoo.com"
PASSWORD = "ftxldmwlfacozfdf"

MY_LAT = 28.701870  # Your latitude
MY_LONG = 77.098360  # Your longitude
MY_LAT_RANGE = ((MY_LAT - 5), (MY_LAT + 5))
MY_LONG_RANGE = ((MY_LONG - 5), (MY_LONG + 5))

# If the ISS is close to my current position
def iss_over_head():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if iss_latitude in MY_LAT_RANGE and iss_longitude in MY_LAT_RANGE:
        return True



# and it is currently dark
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunrise or time_now <= sunset:
        return True

# Then send me an email to tell me to look up.
while True:
    time.sleep(60)                       # BONUS: run the code every 60 seconds.
    if is_night() and iss_over_head():
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(to_addrs=MY_EMAIL,
                                from_addr=MY_EMAIL,
                                msg="Subject: ISS Location\n\n Look UP in the sky, ISS corrosing nearby you in sky")





