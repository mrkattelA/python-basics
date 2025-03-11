import sqlite3
from pathlib import Path

def main():
    db = Path(r"C:\Users\mrkat\OneDrive\Desktop\Webucator\Python2\working-with-data\data\lahmansbaseballdb.sqlite")
    if not db.exists():
        print(
"You have to download the database from https://github.com/WebucatorTraining/lahman-baseball-mysql/blob/master/lahmansbaseballdb.sqlite?raw=true and save it in the data folder."
        )
        return
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    query = """SELECT p.nameFirst, p.nameLast, b.HR,
                    t.name AS team, b.yearID
                FROM batting b
                    JOIN people p ON p.playerID = b.playerID
                    JOIN teams t ON t.ID = b.team_ID
                WHERE b.yearID = ?
                ORDER BY b.HR DESC
                LIMIT 5;"""
    
    
    checking = True
    while checking:
        year_ID = int(input("Enter Year or 0 to quit: "))
        if year_ID == 0:
            break
    
        cursor.execute(query, [year_ID])
        results = cursor.fetchall()

        for i, result in enumerate(results, 1):
            name = f"{result["nameFirst"]} {result["nameLast"]}"
            print(f"{i}.{name} : {result["HR"]}")

    cursor.close()
    connection.close()

main()