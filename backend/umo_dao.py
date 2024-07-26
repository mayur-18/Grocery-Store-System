def get_umo(connection):
    
    cursor =connection.cursor()
    query = ("select *from umo;")
    cursor.execute(query)
    response = []
    for(umo_id,umo_name) in cursor:
       response.append ({
           'umo_id':umo_id,
           'umo_name':umo_name
           })
    return response


if __name__ == '__main__':

    from sql_connection import get_sql_connection
    connection = get_sql_connection()

    print(get_umo(connection))

