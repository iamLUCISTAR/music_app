import sqlite3
from playlist.playlist_dao import PlaylistDAO

conn = sqlite3.connect("/Users/sharathb/PycharmProjects/music_app/db/music.sqlite", check_same_thread=False)
conn.execute("PRAGMA foreign_keys = 1")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


class RecommendationDAO(PlaylistDAO):

    def recommendation_exist(self, entity_type, entity_id, to_id):
        try:
            query = "select recommendation_id from recommendation where entity_type = ? and entity_id = ? and" \
                    " to_user_id = ?"
            cursor.execute(query, (entity_type, entity_id, to_id))
            res = cursor.fetchone()
            if res:
                return dict(res)['recommendation_id']
        except sqlite3.Error as ex:
            raise ex
        except Exception as ex:
            raise ex

    def create_recommendation(self, entity, entity_id, from_id, to_id):
        try:
            query = "insert into recommendation (entity_type, entity_id, by_user_id, to_user_id) values (?,?,?,?)"
            cursor.execute(query, (entity, entity_id, from_id, to_id))
            conn.commit()
            return cursor.lastrowid
        except sqlite3.Error as ex:
            raise ex
        except Exception as ex:
            raise ex

    def get_recommendation(self, user_id):
        try:
            query = "select * from recommendation where to_user_id = ?"
            cursor.execute(query, (user_id,))
            res = cursor.fetchall()
            if res:
                return [dict(row) for row in res]

        except sqlite3.Error as ex:
            return {"error": repr(ex)}
        except Exception as ex:
            raise ex
