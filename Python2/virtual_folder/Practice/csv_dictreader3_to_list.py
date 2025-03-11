import csv

def get_data_from_csv_list(csvfile):
    with open(csvfile, newline="", encoding="utf-8") as csvfile:
        data = csv.DictReader(csvfile)
        return list(data)
    
def main():
    data = get_data_from_csv_list("..\Python2\working-with-data\data\population-by-state.csv")

    for row in data:
        print(row["State"])

main()