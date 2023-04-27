import sqlite3

conn = sqlite3.connect("/Users/arasakumars/PycharmProjects/flask_app/db/music.sqlite", check_same_thread=False)
conn.execute("PRAGMA foreign_keys = 1")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


class SongDAO:
    def get_song_details(self, entity_type='song_id', entity_id=None):
        try:
            query = "select song_id, song_name, artist_name, album_name, genre_name from song s " \
                    "join genre g on g.genre_id = s.genre_id " \
                    "join artist at on at.artist_id = s.artist_id " \
                    "join album al on al.album_id = s.album_id"
            if entity_id:
                query += f" where s.{entity_type} = {entity_id}"

            res = cursor.execute(query)
            return [dict(row) for row in res.fetchall()]
        except sqlite3.Error as ex:
            raise ex
        except Exception as ex:
            raise ex

    def get_album_details(self, entity_id=None):
        try:
            query = "select * from album join artist on album.artist_id = artist.artist_id"
            if entity_id:
                query += f" where album_id = {entity_id}"
            res = cursor.execute(query)
            return [dict(row) for row in res.fetchall()]
        except sqlite3.Error as ex:
            raise ex
        except Exception as ex:
            raise ex

    def get_artist_details(self, entity_id=None):
        try:
            query = "select * from artist"
            if entity_id:
                query += f" where artist_id = {entity_id}"
            res = cursor.execute(query)
            return [dict(row) for row in res.fetchall()]
        except sqlite3.Error as ex:
            raise ex
        except Exception as ex:
            raise ex

    def get_genre_details(self, entity_id=None):
        try:
            query = "select * from genre"
            if entity_id:
                query += f" where genre_id = {entity_id}"
            res = cursor.execute(query)
            return [dict(row) for row in res.fetchall()]

        except sqlite3.Error as ex:
            raise ex
        except Exception as ex:
            raise ex

    def create_song_rating(self, song_id, user_id, rating):
        try:
            select_query = "select * from song_rating where song_id = ? and user_id = ?"
            cursor.execute(select_query, (song_id, user_id))
            if cursor.fetchone():
                query = "update song_rating set rating = ? where song_id = ? and user_id = ?"
            else:
                query = "insert into song_rating (rating, song_id, user_id) values (?,?,?)"
            cursor.execute(query, (rating, song_id, user_id))
            conn.commit()
            return cursor.rowcount

        except sqlite3.Error as ex:
            raise ex
        except Exception as ex:
            raise ex

    def get_song_rating(self, song_id):
        try:
            query = "select count(rating) rating_count, COALESCE(round(avg(rating),1), 0) rating_avg from song_rating " \
                    "where " \
                    "song_id = ?"
            cursor.execute(query, (song_id,))
            return dict(cursor.fetchone())

        except sqlite3.Error as ex:
            raise ex
        except Exception as ex:
            raise ex

    def search_item(self, search_value):
        try:
            query_mapper = {"song": "where song_name like ?",
                            "album": "join album on song.album_id = album.album_id where album_name like ?",
                            "artist": "join artist on song.artist_id = artist.artist_id where artist_name like ?",
                            "genre": "join genre on song.genre_id = genre.genre_id where genre_name like ?"}
            search_result = []
            song_ids = set()
            for key, value in query_mapper.items():
                query = "select song_id from song " + value
                cursor.execute(query, ("%" + search_value + "%",))
                result = cursor.fetchall()
                if result:
                    song_ids.update([dict(row)['song_id'] for row in result])
            if song_ids:
                for song_id in song_ids:
                    search_result.extend(self.get_song_details(entity_id=song_id))
            return search_result

        except sqlite3.Error as ex:
            raise ex
        except Exception as ex:
            raise ex


if __name__ == "__main__":
    print(SongDAO().get_song_details())
