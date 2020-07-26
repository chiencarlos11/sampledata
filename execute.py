#!/usr/bin/env python3

import requests, json
import variables
import datetime
import os

current_date = datetime.datetime.today()

ticker_file = open("tickers.txt", "r")
for ticker in ticker_file:
    headers ={"Accept":"application/json"}
    queryurl = variables.iexcloud_url_stable + "/" + variables.stock_api + "/" + ticker.strip() + "/" + variables.stats_api
    querystring = {"token":variables.iexcloud_publishable}
    
    response = requests.request("GET", queryurl, headers=headers, params=querystring)
    json_data = json.loads(response.text)

    datestring = str(current_date.strftime('%Y%m%d'))
    if not os.path.exists('Output/' + datestring):
        os.makedirs('Output/' + datestring, exist_ok=True)

    filename = ticker.strip() + "_" + datestring + ".csv"

    with open('Output/' + datestring + '/' + filename, 'w') as f1:
        f1.write("NAME," + json_data.get('companyName').upper().replace(',','').strip() + "," + current_date.strftime('%d/%m/%y %H:%M:%S') + "\n") 
        f1.write("FLOAT," + str(json_data.get('float')) + "," + current_date.strftime('%d/%m/%y %H:%M:%S') + "\n") 
        f1.write("SHARES OUTSTANDING," + str(json_data.get('sharesOutstanding')) + "," + current_date.strftime('%d/%m/%y %H:%M:%S') + "\n") 


