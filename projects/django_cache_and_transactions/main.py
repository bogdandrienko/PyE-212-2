import psycopg2

connection = psycopg2.connect(user="postgres",
                              password="31284bogdan",
                              host="127.0.0.1",
                              port="5432",
                              database="django_database")
cursor = connection.cursor()

try:
    connection.autocommit = False
    cursor.execute("insert into zarplata (username, salary) VALUES ('Bogdan5', '666');")
    # cursor.execute("insert into zarplata (username, salary) VALUES ('Bogdan', '666');")

    # print(10 / 0)
    # connection.commit()
except Exception as error:
    print(f"ERROR: {error}")
    connection.rollback()
else:
    pass
finally:
    connection.close()
    cursor.close()
