#!/usr/bin/env python3

import configparser
import ast 

config = configparser.ConfigParser()
config.read('config.ini')
iexcloud_url_stable = config['iexcloud']['url']
iexcloud_publishable = config['iexcloud']['publishable']
stock_api = 'stock'
stats_api = 'stats'
price_api = 'price'
quote_api = 'quote'