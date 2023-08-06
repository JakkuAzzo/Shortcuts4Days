import sqlite3

print('''
    Hey boss, i've made a python script that can add users to the database.
    It's pretty simple, just enter the user's name, age, and email.
    Let me know how this goes.
      ''')

import sqlite3

def create_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            address TEXT,
            email TEXT,
            phone_number TEXT,
            age INTEGER,
            passport_number TEXT
        )
    ''')

    num_records = int(input("Enter the number of records to insert: "))

    for i in range(num_records):
        user_id = input("Enter user_id: ")
        name = input("Enter name: ")
        address = input("Enter address: ")
        email = input("Enter email: ")
        phone_number = input("Enter phone number: ")
        age = int(input("Enter age: "))
        passport_number = input("Enter passport number: ")
        print("current record contains: " + user_id + ", " + name + ", " + address + ", " + email + ", " + phone_number + ", " + str(age) + ", " + passport_number)
        print("number of records left: ", num_records - i - 1)

        cursor.execute('''
            INSERT INTO users (user_id, name, address, email, phone_number, age, passport_number)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (user_id, name, address, email, phone_number, age, passport_number))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
