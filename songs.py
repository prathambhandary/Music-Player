import os

def get_songs(app):
    music_folder = os.path.join(app.static_folder, 'music')
    # List all mp3 files in the folder
    return [file for file in os.listdir(music_folder) if file.endswith('.mp3')]