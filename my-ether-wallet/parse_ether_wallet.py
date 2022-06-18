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



with open('addresses-darklist.json', 'r') as j:
    address_json = json.loads(j.read())



outfile = open('address_list.csv', "w", encoding="utf-8", newline='')

# create the csv writer
writer = csv.writer(outfile, delimiter=",")



writer.writerow(list(data.keys()))

for addr in address_json  :

    dictionary = {}


    for key, value in data.items():

        if (key == "Address"):
            dictionary[key] = addr["address"]
        elif (key == "Risk"):
            dictionary[key] = "Info"
        elif (key == "Source_url"):
            dictionary[
                key] = "https://github.com/MyEtherWallet/"
        elif (key == "Source_name"):
            dictionary[key] = "ether-wallet"
        elif (key == "Source_date"):
            dictionary[key] = addr["date"]
        elif (key == "Added_date"):
            dictionary[key] = datetime.datetime.now().date().strftime('%Y/%m/%d')
        elif (key == "Meta"):
            dictionary[key] = addr["comment"]

    writer.writerow(list(dictionary.values()))



