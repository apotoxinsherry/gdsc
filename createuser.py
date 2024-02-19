import sqlite3

def create_user(username, password, user_type):
    try:
        conn = sqlite3.connect('login_system.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (username, password, user_type)
            VALUES (?, ?, ?)
        """, (username, password, user_type))
        conn.commit()
        print(f"User '{username}' created successfully.")
    except sqlite3.IntegrityError:
        print(f"User '{username}' already exists.")
    except sqlite3.Error as e:
        print("Error creating user:", e)
    finally:
        if conn:
            conn.close()

def main():
    # Create forest officer user
    create_user("forest_officer", "forest123", "forest_officer")

    # Create operator user
    create_user("operator", "operator123", "operator")

if __name__ == "__main__":
    main()
