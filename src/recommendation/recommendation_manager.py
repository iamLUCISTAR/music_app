from .recommendation_dao import RecommendationDAO


class RecommendationManager:

    def __init__(self, request_data):
        self.entity = request_data['entity'] if request_data.get('entity') else None
        self.entity_id = request_data['entity_id'] if request_data.get('entity_id') else None
        self.user_id = request_data['user_id'] if request_data.get('user_id') else None
        self.by_user = request_data['by_user_id'] if request_data.get('by_user_id') else None
        self.to_user = request_data['to_user_id'] if request_data.get('to_user_id') else None
        self.dao_obj = RecommendationDAO()

    def create_recommendation(self, ):
        if self.dao_obj.recommendation_exist(self.entity, self.entity_id, self.to_user):
            return "Recommendation already exist!!"
        return self.dao_obj.create_recommendation(self.entity, self.entity_id, self.by_user, self.to_user)

    def get_recommendation(self, ):

        function_mapper = {"album": self.dao_obj.get_album_details,
                           "artist": self.dao_obj.get_artist_details,
                           "genre": self.dao_obj.get_genre_details,
                           "song": self.dao_obj.get_song_details}
        recommendations = self.dao_obj.get_recommendation(self.user_id)
        response_dict = {"album": [],
                         "artist": [],
                         "genre": [],
                         "song": []}
        if recommendations:
            for recommendation in recommendations:
                entity = recommendation['entity']
                entity_id = recommendation['entity_id']
                details = function_mapper[entity](entity_id)
                by_user_id = recommendation['by_user_id']
                response_dict[entity].append({'details': details, 'by_user': by_user_id})
        return {"recommendations": response_dict}
