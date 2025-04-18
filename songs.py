import os
from database import retrieve_artist

def get_songs(app):
    music_folder = os.path.join(app.static_folder, 'music')
    # List all mp3 files in the folder
    x = [file for file in os.listdir(music_folder) if file.endswith('.mp3')]
    new_list = []
    i = 0
    for song in x:
        sang = song.replace(".mp3", ".jpg")
        print(song)
        new_list.append([song, retrieve_artist(song.replace("mp3", "")), sang])
    return new_list