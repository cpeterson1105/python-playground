# By Christine Peterson & Leonie Beyrle
#Read vegetables.csv (see previous section) into a variable called vegetables.

import csv

with open('vegetables.csv', 'r') as f:
	reader = csv.DictReader(f)
	rows = list(reader)
	vegetables = [dict(row) for row in rows]

#Print the variable vegetables.
print(vegetables)

#Write vegetables as a JSON file called vegetables.json.
import json

with open('vegetables.json','w') as f:
	json.dump(vegetables,f, indent =2)

