import sqlite3

def init_db():
    conn = sqlite3.connect('artist.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS songs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    artist TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def add_song(title, artist):
    conn = sqlite3.connect('artist.db')
    c = conn.cursor()
    c.execute("INSERT INTO songs (title, artist) VALUES (?, ?)", (title, artist))
    conn.commit()
    conn.close()

def retrieve_artist(song_name):
    conn = sqlite3.connect('artist.db')
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