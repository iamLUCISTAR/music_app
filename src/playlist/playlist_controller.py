from flask_restful import Api, Resource
from flask import Blueprint, request, jsonify
from .playlist_manager import PlaylistManager

playlist_blueprint = Blueprint('playlists', __name__, url_prefix="/playlists")
playlist_api = Api(playlist_blueprint)


class Playlist(Resource):
    def post(self):
        try:
            request_data = request.get_json()
            msg = PlaylistManager(request_data).create_playlist()
            return msg
        except Exception as ex:
            raise ex

    def get(self):
        try:
            request_args = dict(request.args)
            request_data = {"user_id": int(request_args['user_id']),
                            "playlist_name": request_args['playlist_name'] if request_args.get(
                                'playlist_name') else None}
            response = PlaylistManager(request_data).get_playlist()
            return jsonify(response)
        except Exception as ex:
            raise ex

    def put(self):
        try:
            request_data = request.get_json()
            msg = PlaylistManager(request_data).update_songs()
            return msg
        except Exception as ex:
            raise ex


playlist_api.add_resource(Playlist, "")
