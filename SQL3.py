import sqlite3


class Database:
    def __init__(self):
        self.connect = sqlite3.connect('Users_Bot2.db')
        self.cursor = self.connect.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS User(
                        id INTEGER PRIMARY KEY,
                        user_name TEXT,
                        Promt_user TEXT,
                        Requests_user INTEGER)""")
        self.connect.commit()

    def check_user_exists(self, id, user_name):
        self.cursor.execute(
                    "SELECT id, user_name FROM User "
                    "WHERE id = ? "
                    "OR user_name = ? ",
                    (id, user_name))
        data = self.cursor.fetchone()
        return data is not None

    def add_user(self, id, user_name):
        self.cursor.execute("INSERT INTO User VALUES(?, ?, ?, ?);",
                                    (id, user_name,'', 0))
        self.connect.commit()

    def close(self):
        self.connect.close()


class Add_promt:
    def __init__(self):
        self.connect = sqlite3.connect('Users_Bot2.db')
        self.cursor = self.connect.cursor()

    def promt(self, id):
        self.cursor.execute("SELECT id, Promt_user FROM User WHERE id = ?", (id,))
        result = self.cursor.fetchone()
        if result is None:
            error = 'Ошибка'
            return error
        return result

    def add_pomt(self, promt, user_id):
        self.cursor.execute("UPDATE User SET Promt_user = ? WHERE id = ?", (promt, user_id))
        self.connect.commit()

    def close(self):
        self.connect.close()


class promt_user:
    def __init__(self):
        self.connect = sqlite3.connect('Users_Bot2.db')
        self.cursor = self.connect.cursor()

    def promt1(self, id):
        self.cursor.execute(f"SELECT Promt_user FROM User WHERE id = ?", (id,))
        row = self.cursor.fetchone()

        if not row[0]:
            return
        else:
            promt = row[0]
            return promt

    def close(self):
        self.connect.close()


class requests_user:
    def __init__(self):
        self.connect = sqlite3.connect('Users_Bot2.db')
        self.cursor = self.connect.cursor()

    def promt1(self, id):
        self.cursor.execute(f"SELECT Requests_user FROM User WHERE id = ?", (id,))
        row = self.cursor.fetchone()

        if not row:
            return
        else:
            requests = row[0]
            return requests

    def close(self):
        self.connect.close()


class Add_requests:
    def __init__(self):
        self.connect = sqlite3.connect('Users_Bot2.db')
        self.cursor = self.connect.cursor()

    def requests(self, id):
        self.cursor.execute("SELECT id, Requests_user FROM User WHERE id = ?", (id,))
        result = self.cursor.fetchone()
        if result is None:
            error = 'Ошибка'
            return error
        return result

    def add_requests(self, requests, user_id):
        self.cursor.execute("UPDATE User SET Requests_user = ? WHERE id = ?", (requests, user_id))
        self.connect.commit()

    def close(self):
        self.connect.close()