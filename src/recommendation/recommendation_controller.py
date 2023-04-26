from flask_restful import Api, Resource
from flask import Blueprint, request, jsonify
from .recommendation_manager import RecommendationManager

recommendation_blueprint = Blueprint('recommendations', __name__, url_prefix="/recommendations")
playlist_api = Api(recommendation_blueprint)


class Recommendation(Resource):
    def get(self):
        request_data = {"user_id": int(dict(request.args)['user_id'])}
        response = RecommendationManager(request_data).get_recommendation()
        return jsonify(response)

    def post(self):
        request_data = request.get_json()
        msg = RecommendationManager(request_data).create_recommendation()
        return msg


playlist_api.add_resource(Recommendation, "")
