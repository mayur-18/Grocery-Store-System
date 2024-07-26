from datetime import datetime
from sql_connection import get_sql_connection

def insert_order(connection, order):
    cursor = connection.cursor()

    # Insert into orders table
    order_query = ("INSERT INTO orders "
                   "(customer_name, total, date) "
                   "VALUES (%s, %s, %s)")
    order_data = (order['customer_name'], order['total'], datetime.now())
    cursor.execute(order_query, order_data)
    
    order_id = cursor.lastrowid

    # Insert into order_details table
    order_details_query = ("INSERT INTO order_details "
                           "(order_id, product_id, quantity, total_price) "
                           "VALUES (%s, %s, %s, %s)")
    
    order_details_data = [
        (order_id, 
         int(order_detail_record['product_id']), 
         float(order_detail_record['quantity']), 
         float(order_detail_record['total_price']))

        for order_detail_record in order['order_details']
    ]
    cursor.executemany(order_details_query, order_details_data)

    connection.commit()
    return order_id


def get_all_order(connection):
    cursor =connection.cursor()
    query = ("select *from orders order by order_id desc")
    cursor.execute(query)
    response = []
    for(order_id,Customer_name,total,date) in cursor:
       response.append ({
           'order_id':order_id,
           'Customer_name':Customer_name,
           'total':total,
           'date' :date,
           
           })
    return response




if __name__ == "__main__":
    connection = get_sql_connection()
    print(get_all_order(connection))
    # print(insert_order(connection, {
    #     'customer_name': 'Ironman',
    #     'total': '400',
    #     'order_details': [
    #         {'product_id': 2, 'quantity': 2, 'total_price': 50},
    #         {'product_id': 4, 'quantity': 3, 'total_price': 60}
    #     ]
    # }))
