import kucoin, requests, json
from kucoin.client import Market, Trade, User

# PROJECT_PATH = "/home/administrateur/work/projects/crypto_bot"
# CONF_FILE = "secrets.json"
#
# with open(f"{PROJECT_PATH}/{CONF_FILE}", "r") as f:
#     conf = json.load(f)
#
#
# kucoin_key = conf.get('kucoin').get('kucoin_api_key')
# kucoin_secret = conf.get('kucoin').get('kucoin_api_secret')
#
# client = User(key=kucoin_key, secret=kucoin_secret, passphrase="Anatole-99/patagoni@")

from config import load_config

conf = load_config(section="cryptopanic")

url = "https://cryptopanic.com/api/v1/posts/"

r = requests.get("https://cryptopanic.com/api/v1/posts/?auth_token=08f50c8a4c4b14e0974d75d3d2f6270ddbf918eb&currencies=BTC&filter=hot")
token = conf.get("api_key")
token = token.replace('"','')
f = requests.get(
    url,
    params={
        "auth_token": token,
        "filter": "hot",
        }
    )

toto = 0