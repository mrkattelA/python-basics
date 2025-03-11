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

csv_file = "../Python2/working-with-data/data/grades.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as csvfile:
    #fieldnames are must in dictwriter
    fieldnames = ["Art", "Music", "Math", "English"]
    #fieldnames = grades[0].keys=> this code will keep the same order of keys inside dictionary.
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(grades)
    fieldnames = grades[0].keys
