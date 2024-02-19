import sqlite3

def create_database():
    try:
        conn = sqlite3.connect('login_system.db')
        print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating database:", e)
    finally:
        if conn:
            conn.close()

def create_table():
    try:
        conn = sqlite3.connect('login_system.db')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                user_type TEXT NOT NULL CHECK(user_type IN ('forest_officer', 'operator'))
            )
        """)
        print("Table 'users' created successfully.")
    except sqlite3.Error as e:
        print("Error creating table:", e)
    
    finally:
        if conn:
            conn.close()

def main():
    create_database()
    create_table()

if __name__ == "__main__":
    main()
