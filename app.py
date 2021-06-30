from flask import Flask, jsonify, request
from numpy.core.numeric import cross
from flask_cors import CORS,cross_origin 
from usuarios import users
app = Flask(__name__)



CORS(app)
cors = CORS(app, resources={
    r"/*": {
       "origins": "*"
    }
})
#app.config['CORS_HEADERS'] = 'application/json; charset=utf-8'
#app.config['CORS_HEADERS'] = 'Content-Type'
# Testing Route
@app.route('/login', methods=['GET'])
@cross_origin()
def ping():
    return "Hola mundosaa"

# Get Data Routes
@app.route('/login_json')
def getProducts(): 
    return jsonify(users)


@app.route('/login_autentication/<string:product_name>/<string:clave>')
def getProduct(product_name,clave):
    productsFound = [
        product for product in users if product['user'] == product_name and product['pass'] == clave]
    if (len(productsFound) > 0):
        return jsonify([{'users': productsFound[0]}])
    return jsonify([{'message': 'Product Not found'}])
   



#inciar el servidor
if __name__ == '__main__':
    app.run(debug=True, port=4000)