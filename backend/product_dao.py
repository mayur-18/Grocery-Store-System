
from sql_connection import get_sql_connection


def get_all_products(connection):
    
    cursor =connection.cursor()
    query = ("select p.*,umo_name from products as p INNER JOIN umo  On p.umo_id = umo.umo_id;")
    cursor.execute(query)
    response = []
    for(product_id,name,umo_id,price_per_unit,umo_name) in cursor:
       response.append ({
           'product_id':product_id,
           'name':name,
           'umo_id':umo_id,
           'price_per_unit' :price_per_unit,
           'umo_name':umo_name
           })
    return response


def insert_into_products(connection,product):

    cursor =connection.cursor()
    query = ("insert into products (product_name,umo_id,price_per_unit) values(%s,%s,%s)")
    data =(product['product_name'],product['umo_id'],product['price_per_unit'])
    cursor.execute(query,data)
    connection.commit()
    return cursor.lastrowid


def delete_product(connection,product_id):

    cursor =connection.cursor()
    query = ("delete from products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()
    return cursor.lastrowid


if __name__ == '__main__':
    connection = get_sql_connection()
    print(delete_product(connection,3))
