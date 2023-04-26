import sqlite3

conn = sqlite3.connect("/Users/sharath/PycharmProjects/flask_app/db/music.sqlite", check_same_thread=False)
conn.execute("PRAGMA foreign_keys = 1")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


class SongDAO:
    def get_song_details(self, song_id=None):
        query = "select song_id, song_name, artist_name, album_name, genre_name from song s " \
                "join genre g on g.genre_id = s.genre_id " \
                "join artist at on at.artist_id = s.artist_id " \
                "join album al on al.album_id = s.album_id"
        if song_id:
            query += f" where song_id = {song_id}"
            cursor.execute(query)
            return dict(cursor.fetchone())
        res = cursor.execute(query)
        return [dict(row) for row in res.fetchall()]

    def get_album_details(self, album_id=None):
        query = "select * from album join artist on album.artist_id = artist.artist_id"
        if album_id:
            query += f" where album_id = {album_id}"
            cursor.execute(query)
            return dict(cursor.fetchone())
        res = cursor.execute(query)
        return [dict(row) for row in res.fetchall()]

    def get_artist_details(self, artist_id=None):
        query = "select * from artist"
        if artist_id:
            query += f" where artist_id = '{artist_id}'"
            cursor.execute(query)
            return dict(cursor.fetchone())
        res = cursor.execute(query)
        return [dict(row) for row in res.fetchall()]

    def get_genre_details(self, genre_id=None):
        query = "select * from genre"
        if genre_id:
            query += f" where genre_id = '{genre_id}'"
            cursor.execute(query)
            return dict(cursor.fetchone())
        res = cursor.execute(query)
        return [dict(row) for row in res.fetchall()]

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
            return "Song rated successfully"

        except sqlite3.Error as ex:
            return "Song or User doesn't exist"

    def get_song_rating(self, song_id):
        try:
            query = "select count(rating) rating_count, COALESCE(avg(rating), 0) rating_avg from song_rating where " \
                    "song_id = ?"
            res = cursor.execute(query, (song_id,))
            conn.commit()
            return dict(res.fetchone())
        except sqlite3.Error as ex:
            return {"error": ex}

    def search_item(self, search_type, value):
        try:
            type_mapper = {"song": "where song_name like ?",
                           "album": "join album on song.album_id = album.album_id where album_name like ?",
                           "artist": "join artist on song.artist_id = artist.artist_id where artist_name like ?",
                           "genre": "join genre on song.genre_id = genre.genre_id where genre_name like ?"}
            query = f"select song_id from song " + type_mapper[search_type]
            cursor.execute(query, ("%" + value + "%",))
            result = cursor.fetchall()
            if result:
                return [self.get_song_details(dict(row)['song_id']) for row in result]
            return "Search result not found"

        except sqlite3.Error as ex:
            return {"error": ex}
        except Exception as ex:
            return {"error": repr(ex)}


if __name__ == "__main__":
    print(SongDAO().get_song_details())
