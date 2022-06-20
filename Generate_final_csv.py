
import os
import glob
import pandas as pd

parent_path = os.path.abspath(os.getcwd())

all_files = []

for nbr, filename in enumerate(os.listdir(parent_path)):

    if (os.path.isdir(filename) and "." not in filename ):


        all_files.append(os.path.join(filename, "address_list.csv"))



combined_csv = pd.concat([pd.read_csv(f) for f in all_files])
# export to csv
combined_csv.to_csv("final_address_list.csv", index=False, encoding='utf-8-sig')