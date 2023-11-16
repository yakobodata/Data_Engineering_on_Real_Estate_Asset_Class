import requests
import json
import pandas as pd

url = "https://marketing-api.securitize.io/opportunities"

payload = ""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://securitize.io/",
    "Origin": "https://securitize.io",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site"
}

response = requests.request("GET", url, data=payload, headers=headers)

# print(response.text)

data = response.text

json_data = json.loads(response.text)

# Check the data type of the variable 'json_data'
print(type(json_data))

# change the data into a json format
json_string = json.dumps(json_data)
print(type(json_string))

# Write the json data to json file
with open("securitize.json", "w") as outfile:
    outfile.write(json_string)

df = pd.read_json('securitize.json')

df.info()

field_names = ['id','issuerId','image','description','issuerName','issuerLogo','issuerLogoDark','issuerDashboardUrl'
,'issuerFavicon','title','shareValue','isFeatured','order','tokenIcon','tags','navValue','totalRaised'
,'regulationType','launchDate','closeDate','minimumInvestment','signedDate','mainCurrency','opportunityId'
,'primaryMarketUrl']

# open the json file using the pandas and change the data into csv format
with open('securitize.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)

df.to_csv('securitize.csv', encoding='utf-8', index=False)