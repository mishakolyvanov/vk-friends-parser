import sqlite3


class database:
    def __init__(self, database_file):
        """Подключаемся к БД и сохраняяем курсор соедиения"""
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def create_table(self, user_id):
        with self.connection:
            self.cursor.execute("CREATE TABLE IF NOT EXISTS id" + str(user_id) + " (user_id text PRIMARY KEY)")

    def add_user(self, friends, user_id):
        with self.connection:
            for friend_id in friends['response']['items']:
                self.cursor.execute("INSERT OR REPLACE INTO id" + str(user_id) + "(user_id) VALUES (?)", (friend_id,))

    def intersect(self, user_ids):
        with self.connection:
            query = ""
            for user_id in user_ids:
                query += "SELECT * FROM id" + str(user_id) + " INTERSECT "
            query = query[0:-10]
            return self.cursor.execute(query).fetchall()

