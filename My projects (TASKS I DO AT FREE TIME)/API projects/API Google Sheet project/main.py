import requests
import os
from datetime import datetime
from requests.auth import HTTPBasicAuth

APP_ID = os.environ.get('NUTRITION_APP_ID')
API_KEY = os.environ.get('NUTRITION_API_KEY')
SHEETY_USER = os.environ.get('SHEETY_USER')
SHEETY_PASS = os.environ.get('SHEETY_PASS')
AUTHORIZATION_SHEETY = os.environ.get('AUTHORIZATION_SHEETY ')


GENDER = 'Male'
WEIGHT_KG = '110'
HEIGHT_CM = '190'
AGE = '31'

url = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheet_endpoint = os.environ.get('sheet_endpoint')

user_input = input('Please enter the information: ')

parameters = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

user_param = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}



response = requests.post(url=url, json=parameters, headers=user_param)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    sheet_response = requests.post(sheet_endpoint,
                                   json=sheet_inputs,
                                   auth=(
                                       SHEETY_USER,
                                       SHEETY_PASS
                                   ))

    print(sheet_response.text)
