from plateforms import Plateform
from kucoin.client import Market, Trade, User
import json, logging
from typing import Dict, List

class Kucoin(Plateform):
    
    PLATEFORM = "kucoin"
    PASSPHRASE = ""
    SECRET = ""
    API_KEY = ""

    # TODO: update loading conf method for config.ini
    def __init__(self):
        self.conf = self.get_conf(key=self.PLATEFORM)
        self.API_KEY = self.conf.get(f"{self.PLATEFORM}").get('kucoin_api_key')
        self.SECRET = self.conf.get(f"{self.PLATEFORM}").get('kucoin_api_secret')
        self.client = User(key=self.API_KEY, 
                           secret=self.SECRET, 
                           passphrase=self.PASSPHRASE)

    def get_conf(self, key):
        with open(f"{self.PROJECT_PATH}/{self.CONF_FILE}", "r") as f:
            conf = json.load(f)
        return conf
    
    def get_accounts(self) -> List[Dict]:
        """
        get accounts with balance > 0
        """
        accounts = self.client.get_account_list()
        return [acc for acc in accounts if float(acc.get("balance")) > 0.0]
    
    def get_account(self, account_id: str) -> Dict:
        return self.client.get_account(accountId=account_id)
    
    def get_deposit_address(self, account_id: str, crypto: str) -> Dict:
        """
        get deposit address
        create it if does not exist yet
        """
        try:
            content: dict = self.client.get_deposit_address(crypto)
        except Exception as exc:
            error = exc.args[0]
            if "null" in error:
                logging.debug(f"no deposit address has been created yet for {crypto}")
            content: dict = self.client.create_deposit_address(currency=crypto)
        return content


        
    
