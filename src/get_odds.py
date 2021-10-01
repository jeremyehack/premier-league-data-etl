import requests
import pandas as pd
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()
odds_api_key = os.getenv('the_odds_api_key')


def get_current_odds(sport, market, region):
    params = {
                'apiKey': odds_api_key,
                'mkt' : market,
                'regions': region,
              }

    url = f'https://api.the-odds-api.com/v4/sports/{sport}/odds/'

    return requests.get(url, params=params).json()


def main():

    odds_json = get_current_odds(sport='soccer_epl', market='h2h', region='us')
    
    pprint(odds_json)

if __name__ == "__main__":
    main()

    