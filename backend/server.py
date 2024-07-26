from flask import Flask, jsonify, request

app = Flask(__name__)

import product_dao
import umo_dao
from sql_connection import get_sql_connection
import json
import orders_dao

connection = get_sql_connection()

@app.route('/getProducts')
def hello_world():
   products = product_dao.get_all_products(connection)
   response =jsonify(products)
   response.headers.add('Access-Control-Allow-Origin','*')
   return response

@app.route('/getUMO', methods=['GET'])
def get_umo():
    response = umo_dao.get_umo(connection)
    response =jsonify(response)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = product_dao.insert_into_products(connection , request_payload)
    response =jsonify(
        {
            'product_id' : product_id
        }
    )
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection , request_payload)
    response =jsonify(
        {
            'product_id' : order_id
        }
    )
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/getAllOrders' , methods = ['GET'])
def get_all_orders():
   orders = orders_dao.get_all_order(connection)
   response =jsonify(orders)
   response.headers.add('Access-Control-Allow-Origin','*')
   return response

@app.route('/deleteProduct' , methods=['POST'])
def delete_product():
    return_id = product_dao.delete_product(connection,request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

if __name__ == '__main__':
    app.run(debug=True)