import psycopg2

try:
    # number = input("Введите номер id: ")

    class RowObj:
        def __init__(self, row: tuple):
            self.username = row[0]
            self.age = row[1]
            self.married = row[2]
            self.credits = row[3]
            self.id = row[4]

    arr = [
        ('x', 12, 'false', 888.888, 85),
        ('y', 13, 'false', 888.888, 86),
        ('z', 14, 'false', 888.888, 87),
        ('a', 15, 'false', 888.888, 88),
        ('b', 16, 'false', 888.888, 89),
    ]
    connection = psycopg2.connect(
        user="postgres",
        password="31284bogdan",
        host="127.0.0.1",  # 'localhost' \ '192.168.158.16'
        port="5432",
        dbname="example",
    )
    connection.autocommit = True
    cursor = connection.cursor()
    for row in arr:
        obj = RowObj(row=row)
        query_string = f'''INSERT INTO public.example_table 
        (username, age, married, credits, id) values 
        ('{obj.username}', {obj.age}, {obj.married}, {obj.credits}, {obj.id})'''
        cursor.execute(query_string)
        # connection.commit()
except Exception as error:
    print(error)
finally:
    cursor.close()
    connection.close()
