import csv

grades = [
    {
        "English" : 97,
        "Math" : 93,
        "Art" : 84,
        "Music" : 86
    },
    {
        "English" : 89,
        "Math" : 83,
        "Art" : 94,
        "Music" : 76
    }
]

csv_files = "../Python2/working-with-data/data/grades.csv"
with open(csv_files, "a", newline="", encoding="utf-8") as csvfiles:
    fieldnames = grades[0].keys()
    writer = csv.DictWriter(csvfiles, fieldnames=fieldnames)
    writer.writerows