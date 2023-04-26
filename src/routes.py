from flask import Flask
from flask_cors import CORS
from user.user_controller import user_blueprint
from songs.songs_controller import songs_blueprint
from playlist.playlist_controller import playlist_blueprint
from recommendation.recommendation_controller import recommendation_blueprint

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.register_blueprint(user_blueprint)
app.register_blueprint(songs_blueprint)
app.register_blueprint(playlist_blueprint)
app.register_blueprint(recommendation_blueprint)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
