# blockchain-addresses
A list of known blockchain addresses.

## Generating the final list of addresses 


 - The db schema is constantly evolving, we update our database according to the schema.json file 

- Most recent schema sql statement : 
  CREATE TABLE blockping ( Address VARCHAR, Risk VARCHAR, Source_url VARCHAR , Source_name VARCHAR, Source_date VARCHAR , Added_date VARCHAR,Meta VARCHAR  );
 
## Generating the final list of addresses 

 - Each folder contains different files and tools for parsing and generating the address
 - Run the script Generate_final_csv.py to combine all the csv files that contains the different addresses of all folders ->  final_address_list.csv
 - We import the final addresses csv file to the cloud storage 

  ![image](https://user-images.githubusercontent.com/27244768/174452272-db0bc990-ccb2-4168-ba9f-1e316c38d8dc.png)

  ![image](https://user-images.githubusercontent.com/27244768/174452291-53625173-6c5a-4e45-be80-a0506e7625be.png)

  ![image](https://user-images.githubusercontent.com/27244768/174452304-bb6db2cb-dd18-42ba-97ae-f2dacd112d56.png)

 - Finally we browse and import the file to the database

  ![image](https://user-images.githubusercontent.com/27244768/174452575-71e4b183-7a0d-4e88-8ce2-6e691bf74e10.png)



**Ethereum Addresses
