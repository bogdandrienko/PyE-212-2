import psycopg2

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
DELETE FROM public.example_table
WHERE id = 888
    '''
    cursor.execute(query_string)
    connection.commit()
except Exception as error:
    print(error)
finally:
    cursor.close()
    connection.close()
