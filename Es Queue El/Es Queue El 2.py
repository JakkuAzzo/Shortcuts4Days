print('''
      Hey boss, i made a python script that can read from the database.
        It's pretty simple, just enter the table name and column name.
        Let me know how this goes.
      ''')

import sqlite3

def read_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    try:
        table_name = input("Enter the table name to read from: ")
        column_name = input("Enter the column name to display: ")
        
        query = f"SELECT {column_name} FROM {table_name}"
        cursor.execute(query)

        rows = cursor.fetchall()
        
        if len(rows) == 0:
            print("No data found.")
        else:
            print(f"Data from column '{column_name}':")
            for row in rows:
                print(row[0])

    except Exception as e:
        print("Error occurred while reading the database:", e)

    conn.close()

if __name__ == "__main__":
    read_database()
