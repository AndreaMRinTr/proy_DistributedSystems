from objects import User


class AuthenticationService:
    def __init__(self, database):
        self.database = database

    def login(self, username, password):
        query = "SELECT * FROM user WHERE userid = %s AND passw = %s"
        user_info = self.database.execute_query(query, (username, password))

        if user_info:
            user = User(user_info[0], user_info[1])
            user.password = user_info[2]
            return user
        else:
            return None
