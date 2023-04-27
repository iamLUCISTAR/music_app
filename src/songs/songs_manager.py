from .songs_dao import SongDAO


class SongManager:

    def __init__(self, request_data):
        self.song_id = request_data['song_id'] if request_data.get('song_id') else None
        self.song_rating = request_data['rating'] if request_data.get('rating') else None
        self.user_id = request_data['user_id'] if request_data.get('user_id') else None
        self.dao_obj = SongDAO()

    def get_song_details(self, ):
        try:
            song_details = self.dao_obj.get_song_details(entity_id=self.song_id)
            msg = "No song details"
            if song_details:
                msg = "Song details found"
            return {"message": msg, "song_details": song_details}
        except Exception as ex:
            raise ex

    def get_rating(self, ):
        try:
            song_rating = self.dao_obj.get_song_rating(self.song_id)
            msg = "No ratings"
            if song_rating['rating_count']:
                msg = "Ratings found"
            return {"message": msg, "rating_info": song_rating}
        except Exception as ex:
            raise ex

    def rate_song(self, ):
        try:
            msg = "Invalid rating !!"
            if 0 < self.song_rating <= 5:
                row_count = self.dao_obj.create_song_rating(self.song_id, self.user_id, self.song_rating)
                msg = "Song rating failed!!"
                if row_count:
                    msg = "Song rated successfully!!"
            return {"message": msg}
        except Exception as ex:
            raise ex


class SearchManager:
    def __init__(self, request_data):
        self.search_value = request_data['search_value'] if request_data.get('search_value') else None
        self.dao_obj = SongDAO()

    def search_item(self, ):
        try:
            search_results = self.dao_obj.search_item(self.search_value)
            msg = "No search results"
            if search_results:
                msg = "Search results found"
            return {"message": msg, "search_results": search_results}
        except Exception as ex:
            raise ex
