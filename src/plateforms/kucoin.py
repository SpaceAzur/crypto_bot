from plateforms import Plateform
from kucoin.client import Market, Trade, User
import json, logging
from typing import Dict, List
from config import load_config

class Kucoin(Plateform):
    
    NAME = "kucoin"

    def __init__(self):
        self.config = load_config(section=self.NAME)
        self.passphrase = self.config.get("passphrase")
        self.api_key = self.config.get("api_key")
        self.secret = self.config.get("secret")
        self.client = User(key=self.api_key,
                           secret=self.secret,
                           passphrase=self.passphrase)

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
            logging.debug(f"deposit address created for {crypto}")
        return content


        
    
