import sqlite3

conn = sqlite3.connect("/Users/arasakumars/PycharmProjects/flask_app/db/music.sqlite", check_same_thread=False)
conn.execute("PRAGMA foreign_keys = 1")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


class UserDao:

    def user_exist(self, email_id):
        try:
            query = "select * from user where email_id = ?"
            cursor.execute(query, (email_id,))
            return cursor.fetchone()

        except Exception as ex:
            print(ex)
            raise

    def create_user(self, user_name, email_id, password, created_datetime):
        try:
            query = "insert into user (user_name,email_id,password,created_datetime) values (?,?,?,?)"
            cursor.execute(query, (user_name, email_id, password, created_datetime))
            conn.commit()

        except Exception as ex:
            print(ex)
            raise

    def get_user_details(self, user_id=None):
        try:
            query = "select user_id, user_name from user"
            if user_id:
                query += f" where user_id = {user_id}"
            cursor.execute(query)
            return [dict(row) for row in cursor.fetchall()]

        except Exception as ex:
            print(ex)
            raise


if __name__ == "__main__":
    res = user_exist("gom@gmail.com")
    print(res)
