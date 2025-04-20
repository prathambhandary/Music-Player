from flask import Flask, render_template
from songs import get_songs
import os, sys

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        songs = get_songs(app)

        if songs:
            current_song = songs[0]
            return render_template("index.html", current_song=current_song, songs=songs)
        
        return render_template("index.html", current_song="No Songs Found", songs=[])
    
    return app
def resource_path(relative_path):
    """Get absolute path to resource (handles PyInstaller case too)"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")