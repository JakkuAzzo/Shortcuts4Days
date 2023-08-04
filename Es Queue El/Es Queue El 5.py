import sqlite3

print('''
        Hey boss, I made a Python script that can manage user accounts.
        it can store usernames and passwords in the database.
        It's pretty simple
        Let me know how this goes.
        ''')

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
                      FOREIGN KEY (user_id) REFERENCES accounts (id)
                      )''')

    conn.commit()
    conn.close()

def register_user(username, password):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

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

def link_usernames_passwords(user_id, username, password):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Create a new record in the 'users' table linking the username and password to the user_id
    query = f"INSERT INTO users (user_id, username, password) VALUES ({user_id}, '{username}', '{password}')"
    cursor.execute(query)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table_accounts()
    create_table_users()

    # Flawed method using user input without proper validation
    print("\nWelcome! Let's create or check an account.")
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    check_or_create_user(username, password)
