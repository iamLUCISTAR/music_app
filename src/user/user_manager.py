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
                return "User exists"
            UserDao.create_user(self.user_name, self.email_id, self.password)
            return "User created"
        except Exception as ex:
            print(ex)
            raise

    def get_user_details(self,):
        try:
            user_details = self.user_dao.get_user_details(self.user_id)
            return {"users": user_details}
        except Exception as ex:
            print(ex)
            raise