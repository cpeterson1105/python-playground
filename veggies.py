# By Christine Peterson & Leonie Beyrle <- I can spell my partner's last name
vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

# Loops through each vegetable (don't forget header)
import csv

with open('vegetables.csv','w') as f:
	writer = csv.writer(f)
	writer.writerow(['name','color'])
	for vegetable in vegetables:
		writer.writerow([vegetable["name"],vegetable["color"]])

# In the loop, write the name of each vegetable and the 
# color into a CSV called vegetables.csv

