from .songs_dao import SongDAO


class SongManager:

    def __init__(self, request_data):
        self.song_id = request_data['song_id'] if request_data.get('song_id') else None
        self.song_rating = request_data['rating'] if request_data.get('rating') else None
        self.user_id = request_data['user_id'] if request_data.get('user_id') else None
        self.dao_obj = SongDAO()

    def get_song_details(self, ):
        song_details = self.dao_obj.get_song_details(self.song_id)
        return {"songs": song_details}

    def get_rating(self, ):
        song_rating = self.dao_obj.get_song_rating(self.song_id)
        return {"song_id": self.song_id,
                "rating_info": song_rating}

    def rate_song(self, ):
        if 0 < self.song_rating <= 5:
            return self.dao_obj.create_song_rating(self.song_id, self.user_id, self.song_rating)
        return "Invalid rating"


class SearchManager:
    def __init__(self, request_data):
        self.search_type = request_data['type'] if request_data.get('type') else None
        self.search_value = request_data['value'] if request_data.get('value') else None
        self.dao_obj = SongDAO()

    def search_item(self, ):
        songs = self.dao_obj.search_item(self.search_type, self.search_value)
        return {"songs": songs}