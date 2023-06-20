import requests
from pprint import pprint

SHEETY_USER = 'Zygimantas'
SHEETY_PASS = 'LNTyDztSq4e%h4sA4w5F!cq&bEj4@f'
SHEETY_ENDPOINT = 'https://api.sheety.co/78976fd21cb07ff91a31f00fdc772fac/flightDeals/prices'


class DataManager:

    def __init__(self):
        self.destination_date = {}

    def get_destination_date(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        date = response.json()
        self.destination_date = date['prices']
        return self.destination_date

    def update_destination_codes(self):
        for city in self.destination_date:
            new_date = {
                'price': {
                    'iataCode': city['iataCode']
                }
            }
            response = requests.put(
                url=f'{SHEETY_ENDPOINT}/{city["id"]}',
                json=new_date
            )
            print(response.text)
