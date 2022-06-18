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

outfile = open('address_list_ofac.csv', "w", encoding="utf-8", newline='')

# create the csv writer
writer = csv.writer(outfile, delimiter=",")

with open('ofac_sdn.csv', 'r') as f:


    DictReader_obj = csv.DictReader(f)

    writer.writerow(list(data.keys()))
    for item in DictReader_obj:

        dictionary = {}

        for key,value in data.items() :

            if ( key == "Address") :
              dictionary[key] = item["address"]
            elif ( key =="Risk") :
                dictionary[key] = "Info"
            elif (key == "Source_url"):
                dictionary[key] = "https://home.treasury.gov/policy-issues/financial-sanctions/specially-designated-nationals-and-blocked-persons-list-sdn-human-readable-lists"
            elif (key == "Source_name"):
                dictionary[key] = item["category"]
            elif (key == "Source_date"):
                dictionary[key] = "06/17/2022"
            elif (key == "Added_date"):
                dictionary[key] = datetime.datetime.now().date().strftime('%m/%d/%Y')
            elif (key == "Meta"):
                dictionary[key] = item["meta"]

        writer.writerow(list(dictionary.values()))






    exit()









with open('out.csv','w') as outfile:


    with open('ofac_sdn.csv','r') as f:


        writer = csv.writer(outfile)

        DictReader_obj = csv.DictReader(f)

        for item in DictReader_obj:

            writer.writerow(item)
    exit()



# Closing file
f.close()