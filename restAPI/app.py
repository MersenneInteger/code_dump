from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World....'

@app.route('/hithere')
def hi():
    return 'Hi there'

@app.route('/json')
def json():
    n = 3 * 2
    retJson = {
        'field1':'abc',
        'field2':'def',
        'n':n
    }
    return jsonify(retJson)

@app.route('/add_two_nums', methods=["POST"])
def add_two_nums():
    
    dataMap = request.get_json(force=True)
    if "x" not in dataMap and "y" not in dataMap:
        return "Error", 305
    x = dataMap['x']
    y = dataMap['y']
    z = x + y
    respJson = {
        "z":z
    }
    return jsonify(respJson), 200

@app.route('/bye')
def bye():
    return 'Bye'

if __name__=="__main__":
    app.run(host='127.0.0.1',port=80)
