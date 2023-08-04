import sqlite3

print('''
        Hey boss, I made a Python script that can create new columns in the database.
        It's pretty simple, just enter the table name and the number of columns.
        Let me know how this goes.
        ''')

def insert_records():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    try:
        table_name = input("Enter the table name to insert records: ")
        num_records = int(input("Enter the number of records to insert: "))

        for i in range(num_records):
            name = input("Enter name: ")
            address = input("Enter address: ")
            email = input("Enter email: ")
            phone_number = input("Enter phone number: ")
            age = int(input("Enter age: "))
            passport_number = input("Enter passport number: ")

            query = f"INSERT INTO {table_name} VALUES ('{name}', '{address}', '{email}', '{phone_number}', {age}, '{passport_number}')"
            cursor.execute(query)

            print("current record contains:", name, address, email, phone_number, age, passport_number)
            print("number of records left:", num_records - i - 1)

    except Exception as e:
        print("Error occurred while inserting records:", e)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_records()