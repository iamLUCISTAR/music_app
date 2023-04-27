from .playlist_dao import PlaylistDAO


class PlaylistManager:

    def __init__(self, request_data):
        self.playlist_name = request_data['playlist_name'] if request_data.get('playlist_name') else None
        self.user_id = request_data['user_id'] if request_data.get('user_id') else None
        self.song_ids = request_data['song_ids'] if request_data.get('song_ids') else None
        self.action = request_data['action'] if request_data.get('action') else None
        self.dao_obj = PlaylistDAO()

    def get_playlist(self, ):
        try:
            playlists = self.dao_obj.get_playlist_details(self.user_id, self.playlist_name)
            msg = "No playlists"
            if playlists:
                msg = "Playlists found"
                for playlist in playlists:
                    playlist_songs = self.dao_obj.get_playlist_songs(playlist['playlist_id'])
                    song_details = []
                    if playlist_songs:
                        for song in playlist_songs:
                            song_details.extend(self.dao_obj.get_song_details(entity_id=song['song_id']))
                    playlist['songs'] = song_details
            return {"msg": msg, "playlists": playlists}
        except Exception as ex:
            raise ex

    def create_playlist(self, ):
        try:
            if self.dao_obj.playlist_exist(self.playlist_name, self.user_id):
                return 'Playlist already exist'
            playlist_id = self.dao_obj.create_playlist(self.playlist_name, self.user_id)
            if self.song_ids:
                self.dao_obj.add_playlist_songs(playlist_id, self.song_ids)
            return "Playlist created"
        except Exception as ex:
            raise ex

    def update_songs(self, ):
        try:
            playlist_id = self.dao_obj.playlist_exist(self.playlist_name, self.user_id)
            msg = 'Playlist not found'
            if playlist_id:
                if self.action == 'add':
                    msg = self.dao_obj.add_playlist_songs(playlist_id, self.song_ids)
                else:
                    msg = self.dao_obj.delete_playlist_songs(playlist_id, self.song_ids)
            return msg
        except Exception as ex:
            raise ex
