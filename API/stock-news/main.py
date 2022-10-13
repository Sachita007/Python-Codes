import requests
from twilio.rest import Client

TWILIO_API_KEY = "a12678c926d155fbc02579c07bf2484d"
account_sid = "ACa58f1ab954e8eec7979c39660d80b85e"
account_auth = "96b6db50d5beb6ea9ea527452b6d2214"
account_num = '+19036626873'

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY= "DO0Q57LNMD86UFUH"
NEWS_API_KEY = "3849784ce12d4fc986f625f9117c559b"
STOCK_PARAMETERS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY

}
NEWS_PARAMETERS ={
    "q": "tesla",
    "apikey": NEWS_API_KEY
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.


response = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMETERS)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list =[item for item in data.items()][:2]

yesterday_close = float(data_list[0][1]["4. close"])
day_before_yesterday_close = float(data_list[1][1]["4. close"])

difference = abs(day_before_yesterday_close-yesterday_close)
diff_percentage = (difference/yesterday_close)*100

def cheack():
    if yesterday_close>day_before_yesterday_close:
        return "🔺"
    else:
        return "🔻"


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing the first 3 articles for the COMPANY_NAME.
#HINT 1: Think about using the Python Slice Operator


if diff_percentage > 0.5:
    news_response = requests.get(NEWS_ENDPOINT,NEWS_PARAMETERS)
    news_data = news_response.json()['articles'][:3]
    news_data_list = [{"title": item["title"],"news":item["description"]} for item in news_data]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # Send a separate message with each article's title and description to your phone number.
    # HINT 1: Consider using a List Comprehension.


    client = Client(account_sid, account_auth)
    for item in news_data_list:
        title = item["title"]
        brief = item["news"]
        message =client.messages.create(body=f"TESLA : {cheack()}{diff_percentage}%\n\n"
                                             f"Headline:{title}\n\n"
                                             f"Brief: {brief}",
                                        from_=account_num,
                                        to="+916202592138")
    print(message.status)
















#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

