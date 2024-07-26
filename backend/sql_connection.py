import mysql.connector

_cnx = None
def get_sql_connection():
    global _cnx
    if _cnx is None:
        _cnx = mysql.connector.connect(user='root', password='1552',
                                host='127.0.0.1',
                                database='grocery_store')
        
    return _cnx