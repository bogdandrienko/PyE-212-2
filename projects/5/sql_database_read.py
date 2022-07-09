import psycopg2
from api import utils

try:
    connection = psycopg2.connect(
        user="postgres",
        password="31284bogdan",
        host="127.0.0.1",  # 'localhost' \ '192.168.158.16'
        port="5432",
        dbname="example",
    )
    cursor = connection.cursor()
    query_string = '''
SELECT * FROM public.example_table
WHERE age = 50
ORDER BY id ASC
    '''
    cursor.execute(query_string)
    records = cursor.fetchall()
    print(records)
    print(type(records))
    for i in records:
        print(i)
        print(type(i))
except Exception as error:
    print(error)
finally:
    cursor.close()
    connection.close()




# obj = utils.SQL(
#     autocommit=True,
#     user="postgres",
#     password="31284bogdan",
#     host="127.0.0.1",  # 'localhost' \ '192.168.158.16'
#     port="5432",
#     dbname="example",
# )
# records = obj.execute('''
# SELECT * FROM public.example_table
# WHERE age = 50
# ORDER BY id ASC
#     ''')
# print(records)
#
#
# records = obj.execute('''
# SELECT * FROM public.example_table
# WHERE id > 50
# ORDER BY id ASC
#     ''')
# print(records)
