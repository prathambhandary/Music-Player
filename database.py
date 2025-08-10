import sqlite3

def init_db():
    conn = sqlite3.connect(r'C:\Users\HP\OneDrive\Desktop\Pratham\0day\Code Challenge\Music-Player\artist.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS songs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    artist TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def add_song(title, artist):
    conn = sqlite3.connect(r'C:\Users\HP\OneDrive\Desktop\Pratham\0day\Code Challenge\Music-Player\artist.db')
    c = conn.cursor()
    c.execute("INSERT INTO songs (title, artist) VALUES (?, ?)", (title, artist))
    conn.commit()
    conn.close()

def retrieve_artist(song_name):
    conn = sqlite3.connect(r'C:\Users\HP\OneDrive\Desktop\Pratham\0day\Code Challenge\Music-Player\artist.db')
    cursor = conn.cursor()
    cursor.execute("SELECT artist FROM songs WHERE title = ?", (song_name,))
    result = cursor.fetchone()

    if result:
        return result[0]
    else:
        artist = input(f"Enter artist for '{song_name}': ")
        add_song(song_name, artist)
        conn.commit()
        return artist
    
def edit_song_name():
    conn = sqlite3.connect(r'C:\Users\HP\OneDrive\Desktop\Pratham\0day\Code Challenge\Music-Player\artist.db')
    cursor = conn.cursor()
    
    id = input("Enter the id you want to update: ")
    cursor.execute("SELECT title FROM songs WHERE id LIKE ?", (f"%{id}%",))
    result = cursor.fetchone()
    
    if result:
        print(f"Current title for '{id}': {result[0]}")
        new_title = input("Enter new title name: ")
        cursor.execute("UPDATE songs SET title = ? WHERE id = ?", (new_title, id))
        conn.commit()
        print(f"Title updated to '{new_title}' for id '{id}'.")
    else:
        print(f"No song found with id '{id}'.")
    conn.commit()
    conn.close()

def delete_row_by_id(row_id):
    try:
        # Connect to the database
        conn = sqlite3.connect("artist.db")
        cursor = conn.cursor()

        # Create a safe SQL delete query
        query = f"DELETE FROM songs WHERE id = ?"
        cursor.execute(query, (row_id,))
        
        # Commit changes and check affected rows
        conn.commit()
        if cursor.rowcount > 0:
            print(f"✅ Deleted row with id={row_id} from 'songs'")
        else:
            print(f"⚠️ No row found with id={row_id} in 'songs'")

    except sqlite3.Error as e:
        print(f"❌ SQLite error: {e}")
    finally:
        conn.close()