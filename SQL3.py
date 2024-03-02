import sqlite3


class Connection_Closure:
    def __init__(self):
        self.connect = sqlite3.connect('Users_Bot8.db')
        self.cursor = self.connect.cursor()

    def close(self):
        self.connect.close()


class Database(Connection_Closure):
    def __init__(self):
        super().__init__()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS User(
                        id INTEGER PRIMARY KEY,
                        user_name TEXT,
                        Requests_user INTEGER,
                        subject TEXT,
                        level TEXT,
                        role TEXT,
                        Question TEXT,
                        Promt_user TEXT)""")
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
        self.cursor.execute("INSERT INTO User VALUES(?, ?, ?, ?, ?, ?, ?, ?);",
                                    (id, user_name, 0, 'Математика', 'Базовый', 'Ассистент', '', ''))
        self.connect.commit()


class Add_promt(Connection_Closure):
    def __init__(self):
        super().__init__()

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


class promt_user(Connection_Closure):
    def __init__(self):
        super().__init__()

    def promt1(self, id):
        self.cursor.execute(f"SELECT Promt_user FROM User WHERE id = ?", (id,))
        row = self.cursor.fetchone()

        if not row[0]:
            return
        else:
            promt = row[0]
            return promt


class requests_user(Connection_Closure):
    def __init__(self):
        super().__init__()

    def promt1(self, id):
        self.cursor.execute(f"SELECT Requests_user FROM User WHERE id = ?", (id,))
        row = self.cursor.fetchone()

        if not row:
            return
        else:
            requests = row[0]
            return requests


class Add_requests(Connection_Closure):
    def __init__(self):
        super().__init__()

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


class Add_subject(Connection_Closure):
    def __init__(self):
        super().__init__()

    def subject(self, id):
        self.cursor.execute("SELECT id, subject FROM User WHERE id = ?", (id,))
        result = self.cursor.fetchone()
        if result is None:
            error = 'Ошибка'
            return error
        return result

    def add_subject(self, promt, user_id):
        self.cursor.execute("UPDATE User SET subject = ? WHERE id = ?", (promt, user_id))
        self.connect.commit()


class subject_user(Connection_Closure):
    def __init__(self):
        super().__init__()

    def subject(self, id):
        self.cursor.execute(f"SELECT subject FROM User WHERE id = ?", (id,))
        row = self.cursor.fetchone()

        if not row:
            return
        else:
            requests = row[0]
            return requests


class Add_level(Connection_Closure):
    def __init__(self):
        super().__init__()

    def level(self, id):
        self.cursor.execute("SELECT id, level FROM User WHERE id = ?", (id,))
        result = self.cursor.fetchone()
        if result is None:
            error = 'Ошибка'
            return error
        return result

    def add_level(self, promt, user_id):
        self.cursor.execute("UPDATE User SET level = ? WHERE id = ?", (promt, user_id))
        self.connect.commit()


class level_user(Connection_Closure):
    def __init__(self):
        super().__init__()

    def level(self, id):
        self.cursor.execute(f"SELECT level FROM User WHERE id = ?", (id,))
        row = self.cursor.fetchone()

        if not row:
            return
        else:
            requests = row[0]
            return requests


class Add_Question(Connection_Closure):
    def __init__(self):
        super().__init__()

    def Question(self, id):
        self.cursor.execute("SELECT id, Question FROM User WHERE id = ?", (id,))
        result = self.cursor.fetchone()
        if result is None:
            error = 'Ошибка'
            return error
        return result

    def add_Question(self, question, user_id):
        self.cursor.execute("UPDATE User SET Question = ? WHERE id = ?", (question, user_id))
        self.connect.commit()


class question_user(Connection_Closure):
    def __init__(self):
        super().__init__()

    def Question(self, id):
        self.cursor.execute(f"SELECT Question FROM User WHERE id = ?", (id,))
        row = self.cursor.fetchone()
        if not row:
            return
        else:
            requests = row[0]
            return requests