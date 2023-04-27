import sqlite3
from songs.songs_dao import SongDAO

conn = sqlite3.connect("/Users/sharathb/PycharmProjects/music_app/db/music.sqlite", check_same_thread=False)
conn.execute("PRAGMA foreign_keys = 1")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


class PlaylistDAO(SongDAO):

    def get_playlist_details(self, user_id, playlist_name=None):
        try:
            query = "select * from playlist where user_id = ?"
            params = (user_id,)
            if playlist_name:
                query += " and playlist_name=?"
                params += (playlist_name,)
            cursor.execute(query, params)
            results = cursor.fetchall()
            return [dict(row) for row in results]
        except sqlite3.Error as ex:
            raise ex
        except Exception as ex:
            raise ex

    def create_playlist(self, playlist_name, user_id):
        try:
            query = "insert into playlist (playlist_name, user_id) values (?,?)"
            res = cursor.execute(query, (playlist_name, user_id))
            conn.commit()
            return res.lastrowid
        except sqlite3.Error as ex:
            raise ex
        except Exception as ex:
            raise ex

    def get_playlist_songs(self, playlist_id):
        try:
            query = "select * from playlist_song where playlist_id = ?"
            cursor.execute(query, (playlist_id,))
            result = cursor.fetchall()
            if result:
                return [dict(row) for row in result]
        except sqlite3.Error as ex:
            raise ex
        except Exception as ex:
            raise ex

    def add_playlist_songs(self, playlist_id, song_ids):
        try:
            query = "insert into playlist_song (song_id,playlist_id) values (?,?)"
            for song_id in song_ids:
                if not self.playlist_song_exists(song_id, playlist_id):
                    cursor.execute(query, (song_id, playlist_id))
            conn.commit()
        except sqlite3.Error as ex:
            raise ex
        except Exception as ex:
            raise ex

    def delete_playlist_songs(self, playlist_id, song_ids):
        try:
            query = "delete from playlist_song where song_id = ? and playlist_id = ?"
            for song_id in song_ids:
                if self.playlist_song_exists(song_id, playlist_id):
                    cursor.execute(query, (song_id, playlist_id))
            conn.commit()
        except sqlite3.Error as ex:
            raise ex
        except Exception as ex:
            raise ex

    def playlist_exist(self, playlist_name, user_id):
        try:
            query = "select playlist_id from playlist where playlist_name = ? and user_id = ?"
            cursor.execute(query, (playlist_name, user_id))
            playlist_id = cursor.fetchone()
            if playlist_id:
                return dict(playlist_id)['playlist_id']
        except sqlite3.Error as ex:
            raise ex
        except Exception as ex:
            raise ex

    def playlist_song_exists(self, song_id, playlist_id):
        try:
            query = "select * from playlist_song where song_id = ? and playlist_id = ?"
            res = cursor.execute(query, (song_id, playlist_id))
            if res.fetchall():
                return True
            return False
        except sqlite3.Error as ex:
            raise ex
        except Exception as ex:
            raise ex
