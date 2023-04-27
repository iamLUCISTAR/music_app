from flask_restful import Api, Resource
from flask import Blueprint, request, jsonify
from .recommendation_manager import RecommendationManager

recommendation_blueprint = Blueprint('recommendations', __name__, url_prefix="/recommendations")
recommendation_api = Api(recommendation_blueprint)


class UserRecommendation(Resource):
    def get(self):
        try:
            request_data = {"user_id": int(dict(request.args)['user_id'])}
            response = RecommendationManager(request_data).get_user_recommendation()
            return jsonify(response)
        except Exception as ex:
            resp = jsonify({'message': repr(ex)})
            resp.status_code = 500
            return resp

    def post(self):
        try:
            request_data = request.get_json()
            msg = RecommendationManager(request_data).create_user_recommendation()
            return msg
        except Exception as ex:
            resp = jsonify({'message': repr(ex)})
            resp.status_code = 500
            return resp


recommendation_api.add_resource(UserRecommendation, "/user")


class SongsRecommendation(Resource):
    def get(self):
        try:
            request_args = request.args
            request_dict = {'user_id': request_args['user_id']}
            response = RecommendationManager(request_dict).get_songs_recommendation()
            return jsonify(response)
        except Exception as ex:
            resp = jsonify({'message': repr(ex)})
            resp.status_code = 500
            return resp


recommendation_api.add_resource(SongsRecommendation, "/songs")


class PlaylistRecommendation(Resource):
    def get(self):
        try:
            request_args = request.args
            request_dict = {'user_id': request_args['user_id']}
            resp = RecommendationManager(request_dict).get_playlist_recommendation()
            return jsonify(resp)
        except Exception as ex:
            resp = jsonify({'message': repr(ex)})
            resp.status_code = 500
            return resp


recommendation_api.add_resource(PlaylistRecommendation, "/playlists")
