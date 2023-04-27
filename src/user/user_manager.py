from flask import session, jsonify
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from .user_dao import UserDao


class UserManager:
    def __init__(self, request_data):
        self.email_id = request_data['email_id'] if request_data.get('email_id') else None
        self.user_name = request_data['user_name'] if request_data.get('user_name') else None
        self.password = request_data['password'] if request_data.get('password') else None
        self.user_id = request_data['user_id'] if request_data.get('user_id') else None
        self.user_dao = UserDao()

    def create_user(self, ):
        try:
            if self.user_dao.user_exist(self.email_id):
                resp = jsonify({"message": "User already exist"})
                resp.status_code = 409
                return resp
            password_hash = generate_password_hash(self.password)
            created_datetime = datetime.now()
            self.user_dao.create_user(self.user_name, self.email_id, password_hash, created_datetime)
            resp = jsonify({"message": "User created"})
            resp.status_code = 201
            return resp
        except Exception as ex:
            raise ex

    def login_user(self, ):
        try:
            user_details = self.user_dao.user_exist(self.email_id)
            if user_details:
                if check_password_hash(user_details['password'], self.password):
                    print(session)
                    if user_details['user_name'] in session:
                        user_name = session[user_details['user_name']]
                        return jsonify({"message": f"{user_name} already logged in"})
                    else:
                        session[user_details['user_name']] = self.password
                        print(session)
                        return jsonify({"message": "Login successful"})

            resp = jsonify({"message": "Bad Request - invalid credentials"})
            resp.status_code = 400
            return resp

        except Exception as ex:
            raise ex

    def logout_user(self, ):
        try:
            user_details = self.user_dao.user_exist(self.email_id)
            if user_details:
                user_name = user_details['user_name']
                if user_name in session:
                    session.pop(user_name)
                    return jsonify({"message": f"{user_name} logged out"})
                else:
                    return jsonify({"message": "User not logged in"})

            resp = jsonify({"message": "Bad Request - User not found"})
            resp.status_code = 400
            return resp

        except Exception as ex:
            raise ex
