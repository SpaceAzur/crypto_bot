import kucoin, requests, json
from kucoin.client import Market, Trade, User

PROJECT_PATH = "/home/administrateur/work/projects/crypto_bot"
CONF_FILE = "secrets.json"

with open(f"{PROJECT_PATH}/{CONF_FILE}", "r") as f:
    conf = json.load(f)


kucoin_key = conf.get('kucoin').get('kucoin_api_key')
kucoin_secret = conf.get('kucoin').get('kucoin_api_secret')

client = User(key=kucoin_key, secret=kucoin_secret, passphrase="Anatole-99/patagoni@")

toto = 0