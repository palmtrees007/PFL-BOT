import pymysql
import pymysql.connections



def db_connect(host, port, user, password, database):
    try:
        connection = pymysql.connect(
            host=host,
            port=int(port),
            user=user,
            password=password,
            database=database,
            cursorclass=pymysql.cursors.DictCursor
        )
        print('connected')
        return connection
    except Exception as e:
        print('error connection')


def check(email, connection: pymysql.connections.Connection):
    try:
        with connection.cursor() as cursor:
            select = f"SELECT EXISTS(SELECT email FROM Users WHERE email = '{email}') AS email;"
            cursor.execute(select)
            res = cursor.fetchall()
            res = res[0]['email']
            if res == 1 or res == '1':
                return False
            elif res == 0 or res == '0':
                return True
            else:
                return None
    finally:
        connection.close()