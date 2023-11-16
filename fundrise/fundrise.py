import requests
import json
import csv
import pandas as pd
import math
url = "https://api.fundrise.com/api/reit-elements"

payload = ""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Origin": "https://fundrise.com",
    "Connection": "keep-alive",
    "Referer": "https://fundrise.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site"
}

response = requests.request("GET", url, data=payload, headers=headers)

# print(response.text)

# data = response.text

json_data = json.loads(response.text)

# Check the data type of the variable 'json_data'
print(type(json_data))

# change the data type of 'json_data' into json data format
json_string = json.dumps(json_data)
print(type(json_string))

# write the json data into a json file
with open("fundrise.json", "w") as outfile:
    outfile.write(json_string)

df = pd.read_json('fundrise.json')

df.info()

    
field_names = ['id','name','reitDollarsInvestedInElement','reitName','reitId','strategy','reitName'                       
   ,'coverPhotoUrl','thumbnailUrl','status','projectType','address' ,'city','state','zip'                            
   ,'lat','lon','submarket','structure','realizedReturn','totalSize','acquisitionDate','exitDate','blendedReturnProjection','annualInterestRate','projectedReturnLowerBound'      
   ,'projectedReturnUpperBound','returnRateType','riskScore','rating','inScopeForInvestorSubmissions','market','geoJson'] 



with open('fundrise.csv', 'a') as file:

    writer = csv.writer(file)

    writer.writerow(field_names)

    for i, row in df.iterrows():

        reits_list = row[2]

        for trust in reits_list:
                      
            data = [row[0], row[1], trust["reitDollarsInvestedInElement"],  trust["name"], row[3], row[4], row[5], row[6]
                , row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15] , row[16] 
                , row[17] , row[18] , row[19] , row[20] , row[21] , row[22] , row[23], row[24] , row[25] 
                , row[26] , row[27] , row[28] , row[29] , row[30] ]

            writer.writerow(data)

# Dealing with Nan values
df = pd.read_csv('fundrise.csv', encoding= 'unicode_escape')

df.name.fillna(df.projectType, inplace = True)

df.to_csv('fundrise.csv',index=False)




