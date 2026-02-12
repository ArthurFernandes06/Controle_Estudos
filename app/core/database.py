import pymysql


def connect_db():
    connection = pymysql.connect(
        host='localhost',
        user='app_user',
        password='ItIJ0ENs*}',
        database='controle_estudos'
    )
    try:
        yield connection
    finally:
        connection.close()