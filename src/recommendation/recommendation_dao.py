import sqlite3
from playlist.playlist_dao import PlaylistDAO

conn = sqlite3.connect("/Users/sharath/PycharmProjects/flask_app/db/music.sqlite", check_same_thread=False)
conn.execute("PRAGMA foreign_keys = 1")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


class RecommendationDAO(PlaylistDAO):

    def recommendation_exist(self, entity, entity_id, to_id):
        query = "select recommendation_id from recommendation where entity = ? and entity_id = ? and to_user_id = ?"
        cursor.execute(query, (entity, entity_id, to_id))
        res = cursor.fetchone()
        if res:
            return dict(res)['recommendation_id']

    def create_recommendation(self, entity, entity_id, from_id, to_id):
        try:
            query = "insert into recommendation (entity, entity_id, by_user_id, to_user_id) values (?,?,?,?)"
            cursor.execute(query, (entity, entity_id, from_id, to_id))
            return "Recommendation created"
        except sqlite3.Error as ex:
            return repr(ex)
        finally:
            conn.commit()

    def get_recommendation(self, user_id):
        try:
            query = "select * from recommendation where to_user_id = ?"
            cursor.execute(query, (user_id,))
            res = cursor.fetchall()
            if res:
                return [dict(row) for row in res]

        except sqlite3.Error as ex:
            return {"error": repr(ex)}
