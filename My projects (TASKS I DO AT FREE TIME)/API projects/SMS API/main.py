import requests
import os
from twilio.rest import Client

api_key = 'e67df1c8b993716b54bd95f9280f775a'
OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/weather'
account_sid = 'AC6bd8f02c1b719f0ae0d7c0ba65da5db4'
auth_token = '6369f8a729305ee7ec93a2dda878777a'


weather_params = {
    'lat': 55.932079,
    'lon': 23.314220,
    'appid': api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
question_data = weather_data['main']['pressure']
value = True if question_data <= 700 else False

if value:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body = "It`s going to rain today. Remember to bring on ☔",
        from_='+15674122326',
        to ='+37063695681'
    )

    print(message.status)
