import sqlite3

# Create a connection to the database (this will create the file if it doesn't exist)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create the users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Insert sample data
users_data = [
    ('alice', 'ilovepython'),
    ('bob', 'mysecretpassword')
]

cursor.executemany('INSERT INTO users (username, password) VALUES (?, ?)', users_data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database created and populated with sample data.")
