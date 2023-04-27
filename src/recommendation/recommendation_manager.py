import requests
import random
from .recommendation_dao import RecommendationDAO


class RecommendationManager:

    def __init__(self, request_data):
        self.entity_type = request_data['entity_type'] if request_data.get('entity_type') else None
        self.entity_id = request_data['entity_id'] if request_data.get('entity_id') else None
        self.user_id = request_data['user_id'] if request_data.get('user_id') else None
        self.by_user = request_data['by_user_id'] if request_data.get('by_user_id') else None
        self.to_user = request_data['to_user_id'] if request_data.get('to_user_id') else None
        self.dao_obj = RecommendationDAO()

    def create_user_recommendation(self, ):
        try:
            if self.dao_obj.recommendation_exist(self.entity_type, self.entity_id, self.to_user):
                return {"message": "User recommendation already exist!!"}
            recommendation_id = self.dao_obj.create_recommendation(self.entity_type, self.entity_id, self.by_user, self.to_user)
            if recommendation_id:
                return {"message": "User recommendation created!!"}
        except Exception as ex:
            raise ex

    def get_user_recommendation(self, ):
        try:
            msg = "No user recommendations found"
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
                    entity = recommendation['entity_type']
                    entity_id = recommendation['entity_id']
                    details = function_mapper[entity](entity_id=entity_id)[0]
                    by_user_id = recommendation['by_user_id']
                    response_dict[entity].append({'details': details, 'by_user': by_user_id})
                msg = "User recommendations found"
            return {"message": msg,
                    "recommendations": response_dict}
        except Exception as ex:
            raise ex

    def get_songs_recommendation(self, ):
        try:
            url = "http://127.0.0.1:5001/playlists?user_id=" + self.user_id
            playlist_details = requests.get(url=url).json()
            msg = "No suggestions for the user, as the player has no playlist"
            suggestion_artist = ''
            suggestion_genre = ''
            suggestion_album = ''
            if playlist_details['playlists']:
                artist = []
                genre = []
                album = []
                for playlist in playlist_details['playlists']:
                    if playlist['songs']:
                        for song in playlist['songs']:
                            artist.append(song['artist_name'])
                            genre.append(song['genre_name'])
                            if song.get('album_name'):
                                album.append(song['album_name'])
                msg = "No song suggestions, as the user has no songs in the playlists"
                if artist:
                    suggestion_artist = max(artist, key=artist.count)
                    suggestion_genre = max(genre, key=genre.count)
                    suggestion_album = max(album, key=album.count)
                    msg = "Songs suggested for the user"
            return {'message': msg,
                    'recommended_artist': suggestion_artist,
                    'recommended_genre': suggestion_genre,
                    'recommended_album': suggestion_album}

        except Exception as ex:
            raise ex

    def get_playlist_recommendation(self,):
        try:
            artists = self.dao_obj.get_artist_details()
            genres = self.dao_obj.get_genre_details()
            playlist_suffix = [" collections", " hits", " vibes", " classics", " bliss", " feels", " party"]
            playlist = []
            for artist in artists:
                playlist_name = artist['artist_name'] + random.choice(playlist_suffix)
                songs = self.dao_obj.get_song_details(entity_type='artist_id', entity_id=artist['artist_id'])
                playlist.append({'playlist_name': playlist_name, 'songs': songs})
            for genre in genres:
                playlist_name = genre['genre_name'] + random.choice(playlist_suffix)
                songs = self.dao_obj.get_song_details(entity_type='genre_id', entity_id=genre['genre_id'])
                playlist.append({'playlist_name': playlist_name, 'songs': songs})
            return {"playlists": playlist}
        except Exception as ex:
            raise ex