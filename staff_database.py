import sqlite3

db_name = "Penash.db"
connection = sqlite3.connect(db_name)

cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Reservation_details (
        Name TEXT,
                    Number TEXT,
                    Date TEXT,
                    Time TEXT,
                    People TEXT,
                    Under4s TEXT
    )
''')

connection.commit()
connection.close()

