import json
import csv
from pathlib import Path
import os
import datetime

parent_path = os.path.abspath(os.getcwd()).split('\\')[:-1]

parent_path = "\\".join(parent_path)

# Opening JSON file
schema = open(os.path.join( parent_path  ,'Schema.json'))

# returns JSON object as
# a dictionary
data = json.load(schema)

outfile = open('address_list_celsius.csv', "w", encoding="utf-8", newline='')

# create the csv writer
writer = csv.writer(outfile, delimiter=",")

with open('CelsiusApprentWallets.csv', 'r') as f:


    DictReader_obj = csv.DictReader(f)

    writer.writerow(list(data.keys()))
    for item in DictReader_obj:

        dictionary = {}

        for key,value in data.items() :

            if ( key == "Address") :
              dictionary[key] = item["Wallet"]
            elif ( key =="Risk") :
                dictionary[key] = "Info"
            elif (key == "Source_url"):
                dictionary[key] = "https://twitter.com/lawmaster/status/1536300771020529665"
            elif (key == "Source_name"):
                dictionary[key] = "Wallet addresses for Celsius DeFi lender (Not validated)"
            elif (key == "Source_date"):
                dictionary[key] = "2022/06/13"
            elif (key == "Added_date"):
                dictionary[key] = datetime.datetime.now().date().strftime('%Y/%m/%d')
            elif (key == "Meta"):
                dictionary[key] = "Amount held :" + str(item['Amount held']) + " |  Notes : "+str(item["Notes"])

        writer.writerow(list(dictionary.values()))

