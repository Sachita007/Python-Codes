import requests
import datetime
USERNAME = "sachita"
TOKEN = "jhhlAKHDAJKHDKJ"

pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
graph_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "id" : "codinggraph1",
    "name": "Daily Coding Progress",
    "unit": "hours",
    "type": "float",
    "color": "sora",
    "timezone": "Asia/Tokyo"


}
headers = {
    "X-USER-TOKEN": TOKEN

}

# response = requests.post(pixela_endpoint, json=user_parameters)
# data = response.json()
# print(data)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# response = requests.post(graph_endpoint, json=graph_parameters, headers=headers)

datetime = datetime.datetime.today()
todays_date = datetime.strftime('%Y%m%d')
print(todays_date)

###---Posting a pixel to pixela

post_pixel_endpoint = f"{graph_endpoint}/codinggraph1"
coding_data_parameters = {
    "date" : "20220509",
    "quantity": "3.50",
}
response = requests.post(url=post_pixel_endpoint, json=coding_data_parameters, headers=headers)
print(response.text)