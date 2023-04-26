from flask_restful import Api, Resource
from flask import Blueprint, request, jsonify
from .songs_manager import SongManager, SearchManager

songs_blueprint = Blueprint('songs', __name__, url_prefix="/songs")
songs_api = Api(songs_blueprint)


class Songs(Resource):

    def get(self):
        request_args = dict(request.args)
        request_data = {"song_id": request_args['song_id'] if request_args.get('song_id') else None}
        response = SongManager(request_data).get_song_details()
        return jsonify(response)


songs_api.add_resource(Songs, "/details", )


class SongsRating(Resource):
    def get(self):
        request_args = dict(request.args)
        request_data = {"song_id": int(request_args['song_id'])}
        response = PlaylistManager(request_data).get_rating()
        return jsonify(response)

    def post(self):
        request_data = request.get_json()
        msg = PlaylistManager(request_data).rate_song()
        return msg


songs_api.add_resource(SongsRating, "/rating", )


class Search(Resource):
    def get(self):
        request_args = request.args
        request_data = {"type": request_args['type'],
                        "value": request_args['value']}
        response = SearchManager(request_data).search_item()
        return jsonify(response)


songs_api.add_resource(Search, "/search")
