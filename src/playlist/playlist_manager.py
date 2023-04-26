from .playlist_dao import PlaylistDAO


class PlaylistManager:

    def __init__(self, request_data):
        self.playlist_name = request_data['playlist_name'] if request_data.get('playlist_name') else None
        self.user_id = request_data['user_id'] if request_data.get('user_id') else None
        self.song_id = request_data['song_id'] if request_data.get('song_id') else None
        self.song_ids = request_data['song_ids'] if request_data.get('song_ids') else None
        self.dao_obj = PlaylistDAO()

    def get_playlist(self, ):
        playlists = self.dao_obj.get_playlist_details(self.user_id)
        if playlists:
            return playlists
        return {"playlists": "User has no playlist"}

    def create_playlist(self, ):
        if self.dao_obj.playlist_exist(self.playlist_name, self.user_id):
            return 'Playlist already exist'
        self.dao_obj.create_playlist(self.playlist_name, self.user_id)
        return "Playlist created"

    def get_playlist_songs(self):
        playlist_id = self.dao_obj.playlist_exist(self.playlist_name, self.user_id)
        if playlist_id:
            playlist_songs = self.dao_obj.get_playlist_songs(playlist_id)
            if playlist_songs:
                song_details = [self.dao_obj.get_song_details(song['song_id']) for song in playlist_songs]
                return {"songs": song_details}
            return {"songs": "No songs in the playlist"}
        return {"songs": "Playlist not found"}

    def add_songs(self, ):
        playlist_id = self.dao_obj.playlist_exist(self.playlist_name, self.user_id)
        if not playlist_id:
            playlist_id = self.dao_obj.create_playlist(self.playlist_name, self.user_id)
        msg = self.dao_obj.create_playlist_songs(playlist_id, self.song_ids)
        return f"Songs added in the playlist :{msg}"
