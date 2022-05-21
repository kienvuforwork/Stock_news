import requests
from datetime import datetime as dt
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_api_key = "ef1670e9343c43cba7e84f3bf674d021"
stock_api_key = "K56BLQ82OJIO8RQ0"
twilio = "jKOROYbPv9Rd4wHAuANs1_WKJcvkmbdJ0wJtSKBu"
## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameter = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey":stock_api_key

}
news_parameter = {
    "qInTitle": COMPANY_NAME,
    "apiKey": news_api_key

}
data = requests.get(url="https://www.alphavantage.co/query", params=stock_parameter).json()["Time Series (Daily)"]
print(data)
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
positive_difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
diff_percent = (positive_difference/float(yesterday_closing_price)) * 100
if diff_percent < 1:
    news = requests.get(url=NEWS_ENDPOINT, params=news_parameter)
    articles = news.json()["articles"]
    three_art = articles[:3]

    formatted_article_list = [f"Headline: {articles['title']}.\nBrief: {article['description']}" for article in three_art]



