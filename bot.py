import tweepy
import requests
import json
import time

API_KEY = ""
SECRET_KEY = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

auth_handler = tweepy.OAuthHandler(consumer_key=API_KEY, consumer_secret=SECRET_KEY)
auth_handler.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth_handler, wait_on_rate_limit=True)

print('logged in')

while True:
    bitcoinprice = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
    price = bitcoinprice.json()
    btcusd = price['bitcoin']['usd']
    print(btcusd)

    message = "$BTC currently trading at: $" + str(btcusd) + " USD. #BTC"
    api.update_status(message)

    print('Tweet posted.')

    ethereumprice = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')
    price = ethereumprice.json()
    ethusd = price['ethereum']['usd']
    print(ethusd)

    message = "$ETH currently trading at: $" + str(ethusd) + " USD. #ETH"
    api.update_status(message)

    print('Tweet posted.')

    time.sleep(6000)
