from objects import User, Event
from datetime import datetime

class AuthenticationService:
    def __init__(self, database):
        self.database = database

    def login(self, username, password):
        query = "SELECT * FROM user WHERE userid = %s AND passw = %s"
        user_info = self.database.execute_query(query, (username, password))

        if user_info:
            t = user_info[0]
            user = User(t[0], t[1])
            self.log_event(user.name)
            return user
        else:
            return None

    def get_events(self):
        eventList =[]
        query = """SELECT event_type, author, fecha, hora
            FROM `event`
            ORDER BY fecha DESC, hora DESC;
            """
        data = self.database.execute_query(query)
        print("printing events")


        for item in data:
            print(type(item[0]))
            text =""
            if item[0] == 1:
                text = f"commented on a post"
            if item[0] ==2:
                text = f"Posted a New Tweet"
            if item[0] == 3:
                text = f"Logged in"

            evt = Event(item[0],item[1],item[2],item[3],text)
            eventList.append(evt)
        return eventList
    def log_event(self, username):
        _datetime = datetime.now()
        _date = _datetime.date().isoformat()
        _time = _datetime.time().isoformat()
        query = """INSERT INTO `event` (`event_type`, `author`, `fecha`, `hora`)
            VALUES (%s, %s, %s, %s);
            """
        values =(3,username,_date,_time)
        self.database.execute_insert(query,values)