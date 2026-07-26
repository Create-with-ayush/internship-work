import sqlite3

conn = sqlite3.connect("bluestock_mf.db")

cursor = conn.cursor()

with open("sql/schema.sql", "r") as file:
    schema = file.read()

cursor.executescript(schema)

conn.commit()

conn.close()

print("Database and tables created successfully!")