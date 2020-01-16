# By Christine & Leonie
#Read vegetables.csv into a variable called vegetables.
import csv
with open('vegetables.csv','r') as f:
	reader = csv.DictReader(f)
	rows = list(reader)
	vegetables = [dict(row) for row in rows]

#Loop through vegetables and filter down to only green vegtables 
#using a whitelist.
green_veggies = []
for veg in vegetables:
	if veg['color'] == "green":
		green_veggies.append(veg)

#Print veggies to the terminal
print(green_veggies)

#Write the veggies to a json file called greenveggies.json
import json

with open('greenveggies.json','w') as f:
	json.dump(green_veggies,f)

# Bonus: output another csv called green_vegetables.csv

with open('green_vegetables.csv','w') as f:
	writer = csv.writer(f)
	writer.writerow(['name','color'])
	for vegetable in green_veggies:
		writer.writerow([vegetable["name"],vegetable["color"]])