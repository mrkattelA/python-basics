import csv

def get_data(csvfiles):
    with open(csvfiles, newline="", encoding="utf-8") as csvfiles:
        data = csv.DictReader(csvfiles)
        return list(data)
    
def get_population(data, state, year):
    for row in data:
        if row["State"] == state:
            return row[year]
    return None

def main():
    data = get_data("..\Python2\working-with-data\data\population-by-state.csv")
    state = input("Enter the State: ")
    year = input("Enter the year between 2010 to 2020: ")
    population = get_population(data, state, year)
    if population:
        print(f"{state}\'s population in {year}: {population}.")
    else:
        print(f"No State found matching '{state}'.")

main()
