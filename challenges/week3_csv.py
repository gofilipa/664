import csv

with open ('NYC_Women_s_Resource_Network_Database_20240730.csv') as f:
    dict_reader = csv.DictReader(f)
    for row in dict_reader:
        if row['Manhattan'] == 'Y':
            print(row['OrganizationName'])

    
    

