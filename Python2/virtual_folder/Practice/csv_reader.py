import csv

csv_file = "..\Python2\working-with-data\data\population-by-state.csv"
with open(csv_file, newline="", encoding="utf-8") as csvfile:
    pops = csv.reader(csvfile)
    for row in pops:
        print(", ".join(row))