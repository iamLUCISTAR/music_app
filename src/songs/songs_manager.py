from .songs_dao import SongDAO


class SongManager:

    def __init__(self, request_data):
        self.song_id = request_data['song_id'] if request_data.get('song_id') else None
        self.song_rating = request_data['rating'] if request_data.get('rating') else None
        self.user_id = request_data['user_id'] if request_data.get('user_id') else None
        self.dao_obj = SongDAO()

    def get_song_details(self, ):
        song_details = self.dao_obj.get_song_details(self.song_id)
        msg = "No song details"
        if song_details:
            msg = "Song details found"
        return {"msg": msg, "song_details": song_details}

    def get_rating(self, ):
        song_rating = self.dao_obj.get_song_rating(self.song_id)
        msg = "No ratings"
        if song_rating['rating_count']:
            msg = "Ratings found"
        return {"msg": msg, "rating_info": song_rating}

    def rate_song(self, ):
        if 0 < self.song_rating <= 5:
            row_count = self.dao_obj.create_song_rating(self.song_id, self.user_id, self.song_rating)
            if row_count:
                return "Song rated successfully!!"
            return "Song rating failed!!"
        return "Invalid rating !!"


class SearchManager:
    def __init__(self, request_data):
        self.search_value = request_data['search_value'] if request_data.get('search_value') else None
        self.dao_obj = SongDAO()

    def search_item(self, ):
        search_results = self.dao_obj.search_item(self.search_value)
        msg = "No search results"
        if search_results:
            msg = "Search results found"
        return {"msg": msg, "search_results": search_results}
