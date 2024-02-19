import sqlite3

def create_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('surveillance_data.db')

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Create a table with the specified schema
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS surveillance_data (
            id INTEGER PRIMARY KEY,
            Time TEXT,
            Date TEXT,
            Camera_Number INTEGER,
            Latitude REAL,
            Longitude REAL
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def insert_sample_data():
    # Connect to SQLite database
    conn = sqlite3.connect('surveillance_data.db')
    cursor = conn.cursor()

    # Sample data to insert
    sample_data = [
        ('16:00:00', '2024-02-23', 2, 37.222, -22.4194),
        ('19:30:00', '2024-02-24', 3, 20.7128, -34.0060),
        ('21:45:00', '2024-02-25', 3, 34.0522, -48.2437)
    ]

    # Insert sample data into the table
    cursor.executemany('''
        INSERT INTO surveillance_data (Time, Date, Camera_Number, Latitude, Longitude)
        VALUES (?, ?, ?, ?, ?)
    ''', sample_data)

    # Commit changes and close the connection
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # create_database()
    insert_sample_data()
