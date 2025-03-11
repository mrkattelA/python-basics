import sqlite3
from pathlib import Path
from datetime import datetime

def main():
    db = Path(r"C:\Users\mrkat\OneDrive\Desktop\Webucator\Python2\working-with-data\data\lahmansbaseballdb.sqlite")
    if not db.exists():
        print("Path is not established, try Again")
        return
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row

    query = """SELECT nameFirst, nameLast, weight,
                    debut AS debut
                FROM people
                ORDER BY weight DESC
                LIMIT 5;"""
    
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()

    for result in results:
        player_name = result["nameFirst"] + "" + result["nameLast"]
        weight = result["weight"]
        year = result["debut"][:4]
        print(f"{player_name} weighed {weight} when he debuted in {year}.")

main()