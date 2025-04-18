from flask import Flask, render_template
from songs import get_songs

app = Flask(__name__)

@app.route("/")
def home():
    songs = get_songs(app)
    
    if songs:
        current_song = songs[0]  # First song as current
        return render_template("index.html", current_song=current_song, songs=songs)
    
    return render_template("index.html", current_song="No Songs Found", songs=[])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)