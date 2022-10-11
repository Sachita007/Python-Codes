import requests
FLGHT_SEARCH_ENDPOINT =  "https://tequila-api.kiwi.com"
FLGHT_SEARCH_API = "kU-LE9Mq2bAVMnSF-mV0TIOJ7Yv1tOl3"
import datetime
from flight_data import FlightData

class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{FLGHT_SEARCH_ENDPOINT}/locations/query"
        header = { "apikey" : FLGHT_SEARCH_API}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(location_endpoint, headers=header, params=query)
        response.raise_for_status()
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def flight_search(self,departure_city, destination_city, from_time,to_time ):
        search_endpoint = f"{FLGHT_SEARCH_ENDPOINT}/v2/search"
        headers = {"apikey": FLGHT_SEARCH_API}

        search_params = {
            "fly_from": departure_city,
            "fly_to":destination_city,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(url=search_endpoint, params=search_params, headers=headers )
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data