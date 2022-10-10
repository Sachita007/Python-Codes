import requests
import datetime


APPLICATION_ID = "16b61b21"
API_KEY = "f843db3cae9ac74cf9518603153f6dcc"

end_point = "https://trackapi.nutritionix.com/v2/natural/exercise"
header_file ={
    "x-app-id" : APPLICATION_ID,
    "x-app-key" : API_KEY
}
current_date = datetime.datetime.now()
today_data = current_date.strftime("%d/%m/%Y")
current_time = current_date.strftime("%X")

user_input = input("Tell me which exercise you did:  ")
post_request ={
    "query" : f"{user_input}",
    "gender" : "male",
    "weight_kg":50,
    "height_cm":155.5,
    "age":19
}

response = requests.post(url=end_point, json=post_request, headers=header_file)
response.raise_for_status()
exercise_data = response.json()['exercises']

shetty_endpoint = "https://api.sheety.co/7c9a7e7caa69719c6b60e9040a146ee2/myWorkouts/sheet1"



for exercise in exercise_data:

    sheet_inputs = {
        "sheet1": {
            "date": today_data,
            "time": current_time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }



    shetty_response = requests.post(url=shetty_endpoint, json=sheet_inputs,)
    shetty_response.raise_for_status()
