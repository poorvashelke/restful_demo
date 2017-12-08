from flask import Flask, jsonify, request

app = Flask(__name__)

customers = [{'name' : 'Ash', 'ID' : '21'}, {'name' : 'John', 'ID' : '10' }, {'name' : 'Victor', 'ID' : '06'}]

@app.route('/', method=['GET'])
def test():
	return jsonify({'message' : 'Great It Works!'})

@app.route('/customers', method=['GET'])
def returnAll():
	return jsonify({'customers' : customers})

@app.route('/customers/<int:ID>', method=['GET'])
def returnID(ID):
	cust = []
	return jsonify({'customers' : cust[0]})

@app.route('/customers', method=['POST'])
def addOne():
	customer = {'name' : request.json['name']}

	customers.append(customer)
	return jsonify({'customers' : customers})

# edit or change information
@app.route('/customers/<string:name>' , method=['PUT'])
def editName(name):
	cust = [customer for customer in customers if customer['name'] == name]
	cust[0]['name'] = request.json['name']
	return jsonify({'customer' : cust[0]})

@app.route('/customers/<string:ID>' , method=['PUT'])
def editName(ID):
	cust = [customer for customer in customers if customer['ID'] == ID]
	cust[0]['ID'] = request.json['ID']
	return jsonify({'customer' : cust[0]})

# delete respected entry
@app.route('/customers/<string:name>' , method=['DELETE'])
def removeOne(name, ID):
	cust = [customer for customer in customers if customer['name'] == name]
	customers.remove(cust[0])
	return jsonify({'customers' : customers})

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')