import mysql.connector

def main():

    connection = mysql.connector.connect(
            host='lahman.csw1rmup8ri6.us-east-1.rds.amazonaws.com',
            user='python',
            passwd='python',
            db='lahmansbaseballdb'
    )

    cursor = connection.cursor(prepared=True)

    query = """SELECT p.nameFirst, p.nameLast, b.HR,
                    t.name AS team, b.yearID
                FROM batting b
                    JOIN people p ON p.playerID = b.playerID
                    JOIN teams t ON t.ID = b.team_ID
                WHERE b.yearID = %s
                ORDER BY b.HR DESC
                LIMIT 5;"""
    
    checking = True

    while checking:
        yearID = int(input("Enter a year or 0 to quit: "))
        if yearID == 0:
            break

        cursor.execute(query, [yearID])
        results = cursor.fetchall()

        for i, result in enumerate(results, 1):
            row = dict(zip(cursor.column_names, result))
            name = f"{row["nameFirst"]} {row["nameLast"]}"
            print(f"{i}.{name}:{row["HR"]}")

    cursor.close()
    connection.close()

main()
