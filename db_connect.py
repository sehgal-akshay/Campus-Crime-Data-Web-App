import cx_Oracle
import db_credentials as cred

def db_cursor():
    connection = cursor = None
    try:
        connection = cx_Oracle.connect(cred.username, cred.password, f"{cred.host}/{cred.sid}")
        connection.current_schema = 'kuppala'
        cursor = connection.cursor()
        return [cursor, connection]
    except Exception as e:
        print('Error occurred')
        raise e
    # finally:
    #     if connection:
    #         connection.close()
    #     if cursor:
    #         cursor.close()

[cursor,connection] = db_cursor()
