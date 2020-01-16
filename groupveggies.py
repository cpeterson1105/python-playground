# By Christine & Leonie

#Read vegtables.csv into a variable called vegtables.
import csv
with open('vegetables.csv','r') as f:
	reader = csv.DictReader(f)
	rows = list(reader)
	vegetables = [dict(row) for row in rows]

#Group vegtables by color as a variable vegtables_by_color.
vegetables_by_color = {}
for veg in vegetables:
	color = veg['color']
	if color in vegetables_by_color:
		vegetables_by_color[color].append(veg)
	else:
		vegetables_by_color[color] = [veg]

#Output vegtables_by_color into a json called vegtables_by_color.json.
import json

with open('vegetables_by_color.json','w') as f:
	json.dump(vegetables_by_color,f)
