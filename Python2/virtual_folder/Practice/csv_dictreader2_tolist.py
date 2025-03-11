import csv

def get_data_from_csv(csvfile):
    with open(csvfile, newline="", encoding="utf-8") as csvfile:
        data = csv.DictReader(csvfile)
        return data
    
def main():
    data = get_data_from_csv("..\Python2\working-with-data\data\population-by-state.csv")

    for row in data:
        print(row["State"])

# This will return the notification ValueError: I/O operation on closed file.

main()