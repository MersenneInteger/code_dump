from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

def checkPostData(data, functionName):
    
    if functionName != 'divide':
        if 'x' not in data or 'y' not in data:
            return 301
        else:
            return 200
    else:
        if 'x' not in data or 'y' not in data:
            return 301
        elif data['y'] == 0:
            return 302
        else:
            return 200

class Add(Resource):

    def post(self):
        postData = request.get_json(force=True)
        statusCode = checkPostData(postData, 'add')
        if statusCode != 200:
            retMap = {
                'Message': 'An error occured: missing arg',
                'Status Code': statusCode
            }
            return jsonify(retMap)
        x = int(postData['x'])
        y = int(postData['y'])
        ret = x + y
        retMap = {
            'Message':ret,
            'Status Code':200
        }
        return jsonify(retMap)

class Subtract(Resource):
    
    def post(self):
        postData = request.get_json(force=True)
        statusCode = checkPostData(postData, 'subtract')
        if statusCode != 200:
            retMap = {
                'Message': 'An error occured: missing arg',
                'Status Code': statusCode
            }
            return jsonify(retMap)
        x = int(postData['x'])
        y = int(postData['y'])
        ret = x - y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)

class Multiply(Resource):
    
    def post(self):
        postData = request.get_json(force=True)
        statusCode = checkPostData(postData, 'multiply')
        if statusCode != 200:
            retMap = {
                'Message': 'An error occured: missing arg',
                'Status Code': statusCode
            }
            return jsonify(retMap)
        x = int(postData['x'])
        y = int(postData['y'])
        ret = x * y
        retMap = {
            'Message': ret,
            'Status Code': 200
        }
        return jsonify(retMap)

class Divide(Resource):
    
    def post(self):
        postData = request.get_json(force=True)
        statusCode = checkPostData(postData, 'divide')
        if statusCode == 301:
            retMap = {
                'Message': 'An error occured: missing arg',
                'Status Code': statusCode
            }
        elif statusCode == 302:
            retMap = {
                'Message': 'An error occured: Division by zero not allowed',
                'Status Code': statusCode
            }
        elif statusCode == 200:
            x = float(postData['x'])
            y = float(postData['y'])
            ret = x / y
            retMap = {
                'Message': ret,
                'Status Code': statusCode
            }
        return jsonify(retMap)

api.add_resource(Add, '/add')
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")

@app.route('/')
def hello_world():
    return "Hello world"

if __name__=="__main__":
    app.run(debug=True)
