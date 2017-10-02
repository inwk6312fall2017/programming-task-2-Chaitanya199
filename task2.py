import csv

new_rows = []
chages = {'Crime type':1}
with open('Crime.csv', 'rb') as myfile:
	reader = csv.reader(myfile)
	for row in reader:
		new_row = row
		for key, value in changes.items():
			new_row = [x.replace(key,value) for x in new_row]
		new_rows.append(new_row)


with open ('Crime.csv', 'wb') as myfile:
	writer = csv.writer(myfile)
	writer.writerows(new_rows)

