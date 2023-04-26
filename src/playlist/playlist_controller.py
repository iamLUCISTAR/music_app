from flask_restful import Api, Resource
from flask import Blueprint, request, jsonify
from .playlist_manager import PlaylistManager

playlist_blueprint = Blueprint('playlists', __name__, url_prefix="/playlists")
playlist_api = Api(playlist_blueprint)


class Playlist(Resource):
    def post(self):
        request_data = request.get_json()
        msg = PlaylistManager(request_data).create_playlist()
        return msg

    def get(self):
        request_args = dict(request.args)
        request_data = {"user_id": int(request_args['user_id'])}
        response = PlaylistManager(request_data).get_playlist()
        return jsonify(response)

    def put(self):
        pass


playlist_api.add_resource(Playlist, "")


class PlaylistSongs(Resource):
    def get(self):
        request_args = dict(request.args)
        request_data = {"user_id": int(request_args['user_id']),
                        "playlist_name": request_args['playlist_name']}
        response = PlaylistManager(request_data).get_playlist_songs()
        return jsonify(response)

    def post(self):
        request_data = request.get_json()
        msg = PlaylistManager(request_data).add_songs()
        return msg


playlist_api.add_resource(PlaylistSongs, "/songs")


