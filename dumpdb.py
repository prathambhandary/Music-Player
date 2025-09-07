import sqlite3

# Replace with your actual database file name
db_path = 'artist.db'

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Print the data from each table
for table_name in tables:
    table = table_name[0]
    print(f"\n🔹 Table: {table}")
    
    # Get column names
    cursor.execute(f"PRAGMA table_info({table});")
    columns = [info[1] for info in cursor.fetchall()]
    print("Columns:", columns)
    
    # Fetch and print all rows
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    
    if rows:
        for row in rows:
            print(dict(zip(columns, row)))
    else:
        print("No data.")

# Close the connection
conn.close()
