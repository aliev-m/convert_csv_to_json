import csv
import json
output=[]
with open('C:/win.csv', 'r', newline='') as file:
    reader = csv.DictReader(file)
    for line in reader:
        output.append(line)
json.dump(output, open('C:/out.json', 'w'), indent=4, sort_keys=False)