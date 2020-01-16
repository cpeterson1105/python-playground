# By Christine Peterson and Leonie Beyrle

# Read superheroes.json
import json
from pprint import pprint

with open('superheroes.json','r') as f:
	superheroes = json.load(f)

# Creates empty array called powers
powers = []

# Loop over the members and append powers of each to powers array
members = superheroes['members']
for hero in members:
	hero_powers = hero['powers']
	powers.append(hero_powers)

# Print those powers to the terminal
pprint(powers)

# Read in the JSON
with open('superheroes.json','r') as f:
	superheroes = json.load(f)

# Write a header to the CSV file
import csv
with open('superheroes.csv','w') as f:
	writer = csv.writer(f)
	writer.writerow(['name','age','secretIdentity','powers','squadName','homeTown','formed','secretBase','active'])

	# Loop over the members, and for each member write a row to the csv file
	members = superheroes['members']

	for hero in members:
		hero_name = hero['name']
		hero_age = hero['age']
		hero_secretIdentity = hero['secretIdentity']
		hero_powers = hero['powers']

		squadName = superheroes["squadName"]
		homeTown = superheroes["homeTown"]
		formed = superheroes["formed"]
		secretBase = superheroes["secretBase"]
		active = superheroes["active"]
		writer.writerow([hero_name, hero_age, hero_secretIdentity, hero_powers,squadName,homeTown,formed,secretBase,active])
