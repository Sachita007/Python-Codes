import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/7c9a7e7caa69719c6b60e9040a146ee2/flightDeals/prices"

class DataManager:
    def __init__(self):
        self.destination_data ={}

    def get_destination_data(self):
        self.response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        self.data = self.response.json()["prices"]
        self.destination_data = self.data
        return self.destination_data


    def get_update(self):
        for city in self.destination_data:
            new_data ={
                "price": {
                    "iataCode" : city["iataCode"]
                }
            }
            shety_update_endpoint = f"{SHEETY_PRICES_ENDPOINT}/{city['id']}"
            update_response = requests.put(url=shety_update_endpoint, json=new_data)
            update_response.raise_for_status()
            print(update_response.text)

































    # def __init__(self):
    #     self.flight_api_endpoint = /"
    #     self.sheety_api_endpoint =
    #     self.iata_code_city = []
    #     self.sheet_response = requests.get(self.sheety_api_endpoint).json()
    #     self.city_data = self.sheet_response['prices']
    #     self.city_name = [items["city"] for items in self.city_data]
    #     self.city_id = [items['id'] for items in self.city_data]
    #     self.ita_code()
    #     self.sheet_ita_update()
    #
    # def ita_code(self):
    #     for city in self.city_name:
    #         flight_parameters = {
    #             "term": f"{city}"
    #         }
    #         flight_api_header =
    #
    #         ita_response = requests.get(self.flight_api_endpoint, params=flight_parameters,
    #                                     headers=flight_api_header).json()["locations"][0]['code']
    #         self.ita_code_city.append(ita_response)

    # def sheet_ita_update(self):
    #     for i in range(0, len(self.city_id)):
    #         sheet_input = {
    #             "price": {
    #                 "iataCode": f"{self.ita_code_city[i]}"
    #             }
    #         }
    #
    #         self.sheet_put_response = requests.put(
    #             url=f"https://api.sheety.co/7c9a7e7caa69719c6b60e9040a146ee2/flightDeals/prices/{self.city_id[i]}",
    #             json=sheet_input)

