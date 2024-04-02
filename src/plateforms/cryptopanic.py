from plateforms import Plateform
from config import load_config
import requests, json

class CryptoPanic(Plateform):

    NAME = "cryptopanic"
    APIURL = "https://cryptopanic.com/api/"


    def __init__(self):
        self.config = load_config(section=self.NAME)
        self.token = self.config.get("api_key")

    def get_news_feed(self) -> dict:
        url = self.APIURL + "posts/"
        return requests.get(url, params={"auth_token": self.token})

    def get_news_by_currency(self, currency) -> dict:
        url = self.APIURL + "posts/"
        return requests.get(url,
                            params={
                                "auth_token": self.token,
                                "currencies": currency
                            }).json()

    def login(self):
        pass

    def logout(self):
        pass

    def get_sentiment(self):
        pass
