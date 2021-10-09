from coinbase.wallet.client import Client
from coinbase.wallet.error import AuthenticationError
import json, time
from bot.logic import sum_numbers

# Use full links for Bot Api:
# https://developers.coinbase.com/api/v2?python
# https://github.com/coinbase/coinbase-python
# https://developers.coinbase.com/


class BotClient:

    client = None
    user = None

    def __init__(self, api_key, api_secret):

        try:
            self.client = Client(api_key, api_secret)
            self.user = json.dumps(self.client.get_current_user())
        except AuthenticationError:
            print("Invalid api key")

    def get_accounts(self):

        return self.client.get_accounts()

    def get_list_buys(self):

        return self.client.get_buys(self.user["data"]["id"])

    def run(self):

        if self.user is not None:
            while True:
                sum_numbers(2, 4)
                self.get_accounts()
                time.sleep(1)
