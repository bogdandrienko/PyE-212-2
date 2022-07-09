import psycopg2

try:
    connection = psycopg2.connect(
        user="postgres",
        password="31284bogdan",
        host="127.0.0.1",  # 'localhost' \ '192.168.158.16'
        port="5432",
        dbname="example",
    )
    connection.autocommit = True
    cursor = connection.cursor()
    query_string = '''
UPDATE public.example_table
SET credits = '0.0'
WHERE married = 'true'
    '''
#     query_string = '''
# CREATE TABLE public.table1
# (
#     title text NOT NULL,
#     id serial NOT NULL,
#     PRIMARY KEY (id)
# );
#
# ALTER TABLE IF EXISTS public.table1
#     OWNER to postgres;
#     '''
    cursor.execute(query_string)
    # connection.commit()
except Exception as error:
    print(error)
finally:
    cursor.close()
    connection.close()
