import psycopg2

class Django:
    class Logging:
        @staticmethod
        def write_error_to_log_text_file(error, path="static/"):
            with open(f"{path}log.txt", "a") as file:
                file.write(f"{error}\n")


class SQL:
    def __init__(self, autocommit, user="postgres", password="31284bogdan", host="127.0.0.1", port="5432", dbname="example"):
        self.user = user
        self.password = password

        self.host = host
        self.port = port

        self.dbname = dbname

        self.connection = self.create_connection(autocommit)
        self.cursor = self.create_cursor()

    def create_connection(self, autocommit=True):
        connection = psycopg2.connect(
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            dbname=self.dbname,
        )
        connection.autocommit = autocommit
        return connection

    def create_cursor(self):
        return self.connection.cursor()

    def execute(self, query_string: str, many=True):
        if many:
            self.cursor.execute(query_string)
            return self.cursor.fetchall()
        else:
            self.cursor.execute(query_string)
            return self.cursor.fetchone()
