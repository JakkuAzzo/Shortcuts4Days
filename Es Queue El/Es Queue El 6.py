import sqlite3

print('''
        Hey Boss, this is the ultimate database management script.
        Login to the database and you can immediately get all the info for the account you logged in with.
        Let me know how this goes.
    ''')

import sqlite3

def create_table_accounts():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Create the 'accounts' table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS accounts (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT UNIQUE,
                      password TEXT
                      )''')

    conn.commit()
    conn.close()

def create_table_users():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Create the 'users' table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      user_id INTEGER,
                      username TEXT,
                      password TEXT,
                      name TEXT,
                      address TEXT,
                      email TEXT,
                      phone_number TEXT,
                      age INTEGER,
                      passport_number TEXT,
                      FOREIGN KEY (user_id) REFERENCES accounts (id)
                      )''')

    conn.commit()
    conn.close()

def register_user(username, password):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # FLAWED: SQL injection vulnerability, no input validation or sanitization
    query = f"INSERT INTO accounts (username, password) VALUES ('{username}', '{password}')"
    cursor.execute(query)

    conn.commit()
    conn.close()

def login_user(username, password):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM accounts WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)

    user_data = cursor.fetchall()
    conn.close()

    return user_data

def check_or_create_user(username, password):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # FLAWED: SQL injection vulnerability, no input validation or sanitization
    query = f"SELECT id FROM accounts WHERE username='{username}' OR 1=1 --' AND password='{password}'"
    cursor.execute(query)
    user_id = cursor.fetchone()

    if user_id is None:
        # If the username doesn't exist, create a new account
        register_user(username, password)
        print(f"Account '{username}' created successfully.")
    else:
        print(f"Account '{username}' already exists.")

    conn.close()

def link_user_info(username, password, name):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Get the user_id from the 'accounts' table
    query = f"SELECT id FROM accounts WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    user_id = cursor.fetchone()

    if user_id:
        # Check if the user info is already linked
        query = f"SELECT * FROM users WHERE name='{user_id[0]}'"
        cursor.execute(query)
        user_data = cursor.fetchall()

        if not user_data:
            print("user data not found, lets make new user data")
            address = input("Enter address: ")
            email = input("Enter email: ")
            phone_number = input("Enter phone number: ")
            age = int(input("Enter age: "))
            passport_number = input("Enter passport number: ")

            # Create a new record in the 'users' table linking the username and password to the user_id
            query = f"INSERT INTO users (user_id, username, password, name, address, email, phone_number, age, passport_number) VALUES ({user_id[0]}, '{username}', '{password}', '{name}', '{address}', '{email}', '{phone_number}', {age}, '{passport_number}')"
            cursor.execute(query)
            print(f"User information linked to '{username}' successfully.")
        else:
            print("User information is already linked.")
    else:
        print("Login failed. Please check your username and password.")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table_accounts()
    create_table_users()

    while True:
        print("\n1. Register a new account")
        print("2. Login and link user info")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            check_or_create_user(username, password)

        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            name = input("Enter the name of the account you want to link to: ")
            link_user_info(username, password, name)

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
