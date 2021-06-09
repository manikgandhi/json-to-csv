import json
import csv
with open("./movie.json") as file:
 data = json.load(file)

fname = "output.csv"

with open(fname, "w") as file:
 csv_file = csv.writer(file)
 csv_file.writerow(["Title", "Year", "Rated", "Released", "Runtime", "Genre", "Director", "Writers", "Actors", "Plot", "Language", "Country", "Awards", "Poster", "imdbRating", "imdbVotes", "imdbID"])
 for item in data["description"]:
   csv_file.writerow([item['Title'], item['Year'], item['Rated'], item['Released'], item['Runtime'], item['Genre'], item['Director'], item['Writers'], item['Actors'], item['Plot'], item['Language'], item['Country'], item['Awards'], item['Poster'], item['imdbRating'], item['imdbVotes'], item['imdbID']])

   