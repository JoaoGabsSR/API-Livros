from pymysql import cursors, connect


def db_connection():
    try:
        connection = connect(
            host='localhost',
            user='user',
            password='password',
            database='database',
            charset='utf8mb4',
            cursorclass=cursors.DictCursor
        )

        return connection
    except Exception as e:
        raise e
