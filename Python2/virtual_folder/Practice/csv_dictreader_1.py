import csv

csv_file = "..\Python2\working-with-data\data\population-by-state.csv"

with open(csv_file, newline="", encoding="utf-8") as csvfile:
    pops = csv.DictReader(csvfile)
    print("Headers: ", pops.fieldnames)
    for row in pops:
        pop_2020 = int(row["2020"].replace(",", ""))
        pop_2010 = int(row["2010"].replace(",", ""))

        growth = pop_2020 - pop_2010

        print(f"{row["State"]}: {pop_2020:,} - {pop_2010:,} = {growth:,}")