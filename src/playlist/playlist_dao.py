import sqlite3
from songs.songs_dao import SongDAO

conn = sqlite3.connect("/Users/sharath/PycharmProjects/flask_app/db/music.sqlite", check_same_thread=False)
conn.execute("PRAGMA foreign_keys = 1")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


class PlaylistDAO(SongDAO):

    def get_playlist_details(self, user_id):
        query = "select * from playlist where user_id = ?"
        cursor.execute(query, (user_id,))
        results = cursor.fetchall()
        if results:
            return {"playlists": [dict(row) for row in results]}

    def create_playlist(self, playlist_name, user_id):
        query = "insert into playlist (playlist_name, user_id) values (?,?)"
        res = cursor.execute(query, (playlist_name, user_id))
        conn.commit()
        return res.lastrowid

    def delete_playlist(self, playlist_id):
        playlist_query = "delete from playlist where playlist_id = ?"
        song_query = "delete from playlist_song where playlist_id = ?"
        cursor.execute(song_query, (playlist_id,))
        cursor.execute(playlist_query, (playlist_id,))
        conn.commit()

    def update_playlist_name(self, playlist_id, new_playlist_name):
        query = "update playlist set playlist_name = ? where playlist_id = ?"
        cursor.execute(query, (new_playlist_name, playlist_id))
        conn.commit()
        if cursor.rowcount:
            return "Playlist name updated"
        return "Error in updating playlist name"

    def get_playlist_songs(self, playlist_id):
        query = "select * from playlist_song where playlist_id = ?"
        cursor.execute(query, (playlist_id,))
        result = cursor.fetchall()
        if result:
            return [dict(row) for row in result]

    def create_playlist_songs(self, playlist_id, song_ids):
        query = "insert into playlist_song (song_id,playlist_id) values (?,?)"
        resp = {}
        for song_id in song_ids:
            if not self.playlist_song_exists(song_id, playlist_id):
                cursor.execute(query, (song_id, playlist_id))
                resp[song_id] = "Song added"
            else:
                resp[song_id] = "Song already exist"
        conn.commit()
        return resp

    def playlist_exist(self, playlist_name, user_id):
        query = "select playlist_id from playlist where playlist_name = ? and user_id = ?"
        cursor.execute(query, (playlist_name, user_id))
        playlist_id = cursor.fetchone()
        if playlist_id:
            return dict(playlist_id)['playlist_id']

    def playlist_song_exists(self, song_id, playlist_id):
        query = "select * from playlist_song where song_id = ? and playlist_id = ?"
        res = cursor.execute(query, (song_id, playlist_id))
        if res.fetchall():
            return True
        return False

    def delete_playlist_songs(self, playlist_id, song_ids):
        query = "delete from playlist_song where song_id = ? and playlist_id = ?"
        resp = {}
        for song_id in song_ids:
            if not self.playlist_song_exists(song_id, playlist_id):
                resp[song_id] = "Not in playlist"
            else:
                cursor.execute(query, (song_id, playlist_id))
                resp[song_id] = "Deleted from playlist"
        conn.commit()
        return resp
