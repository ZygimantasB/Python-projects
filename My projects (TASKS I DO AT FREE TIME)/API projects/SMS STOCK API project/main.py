import requests
from datetime import datetime
from pandas.tseries.offsets import BDay
from twilio.rest import Client
from newsapi import NewsApiClient

STOCK_NAME = "TESLA"
COMPANY_NAME = "Tesla Inc"

api_key = 'NWI23EWA1IHJ7PB7'  # alpha vantage
news_api = '8361e55fe9c44c6bb7250ccd35e0ab09'
account_sid_twilio = 'AC6bd8f02c1b719f0ae0d7c0ba65da5db4'
auth_token_twilio = '6369f8a729305ee7ec93a2dda878777a'

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameters_alpha = {
    'function': 'TIME_SERIES_INTRADAY',
    'symbol': 'IBM',
    'interval': '60min',
    'slice': 'year1month1',
    'apikey': api_key
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters_alpha)
response.raise_for_status()
stocks_data = response.json()

today = datetime.today()
yesterday_work_day = today - BDay(1)
yesterday_work_day = datetime.strftime(yesterday_work_day, '%Y-%m-%d')
yesterday_data = stocks_data['Time Series (60min)'][f'{yesterday_work_day} 19:00:00']['4. close']
print(yesterday_data)

before_yesterday = today - BDay(2)
before_yesterday = datetime.strftime(before_yesterday, '%Y-%m-%d')
before_yesterday_date = stocks_data['Time Series (60min)']\
    [f'{before_yesterday} 19:00:00']['4. close']
print(before_yesterday_date)

stock_difference = abs(float(yesterday_data) - float(before_yesterday_date))
print(stock_difference)

percentage_change = stock_difference / float(before_yesterday_date) * 100
print(percentage_change)

parameters_news = {
    'q': COMPANY_NAME,
    'from': yesterday_data,
    'sortBy': 'popularity',
    'apiKey': news_api
}

value = True if percentage_change < 5 else False

if value:
    increment = 0
    news_response = requests.get(NEWS_ENDPOINT, params=parameters_news)
    news_response.raise_for_status()
    data_news = news_response.json()
    company_news = data_news['articles'][:3]
    # for article in company_news:
    #     increment += 1
    #     author = article['author']
    #     title = article['title']
    #     description = article['description']
    #     url = article['url']
    #     publishedAt = article['publishedAt']
    #     content = article['content']
    #     print(increment, '-', 'Author:', author)
    #     print(increment, '-', 'Title:', title)
    #     print(increment, '-', 'Description:', description)
    #     print(increment, '-', 'URL:', url)
    #     print(increment, '-', 'Published At:', publishedAt)
    #     print(increment, '-', 'Content:', content)

article_description = [f"Title: {value['title']}\n Description:{value['description']}" for value in
                       company_news]
print(article_description)

if value:
    client = Client(account_sid_twilio, auth_token_twilio)
    message = client.messages \
        .create(
        body = f'{article_description}',
        from_='+15674122326',
        to ='+37063695681'
    )

    print(message.status)
