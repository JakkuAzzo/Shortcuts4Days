import sqlite3

print('''
      Hey boss, you wanted to see all of the user data right?
        I made a python script that can do that.
        It's pretty simple, just press run.
        Let me know how this goes.
      ''')

def get_user_data(username):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Flawed Query: User input is directly embedded in the SQL query
    query = f"SELECT * FROM users WHERE username='{username}'"
    cursor.execute(query)

    user_data = cursor.fetchall()
    conn.close()

    return user_data
