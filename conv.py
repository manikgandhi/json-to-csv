import json
import csv
 
 
# Opening JSON file and loading the data
# into the variable data
with open('movie.json') as json_file:
    data = json.load(json_file)
 
movie_data = data['description']
 
# now we will open a file for writing
data_file = open('data_file.csv', 'w')
 
# create the csv writer object
csv_writer = csv.writer(data_file)
 
# Counter variable used for writing
# headers to the CSV file
count = 0
 
for mov in movie_data:
    if count == 0:
 
        # Writing headers of CSV file
        header = mov.keys()
        csv_writer.writerow(header)
        count += 1
 
    # Writing data of CSV file
    csv_writer.writerow(mov.values())
 
data_file.close()
 