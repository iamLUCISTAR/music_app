from flask_restful import Api, Resource
from flask import Blueprint, request, jsonify
from .songs_manager import SongManager, SearchManager

songs_blueprint = Blueprint('songs', __name__, url_prefix="/songs")
songs_api = Api(songs_blueprint)


class Songs(Resource):

    def get(self):
        try:
            request_args = dict(request.args)
            request_data = {"song_id": request_args['song_id'] if request_args.get('song_id') else None}
            response = SongManager(request_data).get_song_details()
            return jsonify(response)
        except Exception as ex:
            resp = jsonify({'message': repr(ex)})
            resp.status_code = 500
            return resp


songs_api.add_resource(Songs, "", )


class SongsRating(Resource):
    def get(self):
        try:
            request_args = dict(request.args)
            request_data = {"song_id": int(request_args['song_id'])}
            response = SongManager(request_data).get_rating()
            return jsonify(response)
        except Exception as ex:
            resp = jsonify({'message': repr(ex)})
            resp.status_code = 500
            return resp

    def post(self):
        try:
            request_data = request.get_json()
            msg = SongManager(request_data).rate_song()
            return msg
        except Exception as ex:
            resp = jsonify({'message': repr(ex)})
            resp.status_code = 500
            return resp


songs_api.add_resource(SongsRating, "/rating", )


class Search(Resource):
    def get(self):
        try:
            request_args = request.args
            request_data = {"search_value": request_args['search_value']}
            response = SearchManager(request_data).search_item()
            return jsonify(response)
        except Exception as ex:
            resp = jsonify({'message': repr(ex)})
            resp.status_code = 500
            return resp


songs_api.add_resource(Search, "/search")
