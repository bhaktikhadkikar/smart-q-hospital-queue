import sqlite3

connection = sqlite3.connect("database.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    mobile TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL,
    address TEXT NOT NULL,
    emergency_contact TEXT NOT NULL
)
""")

connection.commit()
connection.close()

print("Patient database created successfully!")