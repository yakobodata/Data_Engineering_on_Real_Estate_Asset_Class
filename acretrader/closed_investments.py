import requests
import json
import pandas as pd
import csv
url = "https://farm.acretrader.com/closed"

querystring = {"limit":"1000","s":"recently-closed:desc"}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://acretrader.com/",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://acretrader.com",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "TE": "trailers"
}

response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)

data = response.text

json_data = json.loads(response.text)

# Check the Data Type of json_data variable
print(type(json_data))

# Change the variable 'json_data' into a json format
json_string = json.dumps(json_data)
print(type(json_string))


# Writing the json data to the json file
with open("closed_investments.json", "w") as outfile:
    outfile.write(json_string)

# To get the keys of the json file , we shall use pandas package to read the json file and get the headers
df = pd.read_json('closed_investments.json')

df.info()

field_names = ['count','data']

# Open and read the json file to change its format to csv using pandas
with open('closed_investments.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)

# for i, row in df.iterrows():
#     print((row[1]).keys())

field_names = ['Stage','launch_date', 'id', 'name', 'slug', 'thumbnail', 'subscribed_shares', 'remaining_shares', 'percent_subscribed'
, 'invested_style', 'ownership_duration', 'farm_crop_type', 'area_size', 'price', 'price_per_acre', 'price_per_share'
, 'raised', 'units', 'min_investment', 'min_shares_amount', 'closing_date', 'pending_closing_date', 'approved_date'
, 'publication_date', 'latitude', 'longtitude', 'state', 'county', 'launch_event', 'relative_risk', 'type', 'status', 'debt'
, 'improvements', 'additional_risk', 'seo_description', 'seo_title', 'invest', 'show_only_to_investors']

with open('closed_investments.csv', 'a') as file:

    writer = csv.writer(file)

    writer.writerow(field_names)

    for i, row in df.iterrows():

        land_list = row[1] 
              
        data = [
            'Closed Investment'
            , land_list['launch_date']
            , land_list['id']
            , land_list['name']
            , land_list['slug']
            , land_list['thumbnail']
            , land_list['subscribed_shares']
            , land_list['remaining_shares']
            , land_list['percent_subscribed']
            , land_list['invested_style']
            , land_list['ownership_duration']
            , land_list['farm_crop_type']
            , land_list['area_size']
            , land_list['price']
            , land_list['price_per_acre']
            , land_list['price_per_share']
            , land_list['raised']
            , land_list['units']
            , land_list['min_investment']
            , land_list['min_shares_amount']
            , land_list['closing_date']
            , land_list['pending_closing_date']
            , land_list['approved_date']
            
            , land_list['latitude']
            , land_list['longtitude']
            , land_list['state']
            , land_list['county']
            
            , land_list['relative_risk']
            , land_list['type']
            , land_list['status']
            , land_list['debt']
            , land_list['improvements']
            , land_list['additional_risk']
            , land_list['seo_description']
            , land_list['seo_title']
            , land_list['invest']
            , land_list['show_only_to_investors']
        ]
        writer.writerow(data)
