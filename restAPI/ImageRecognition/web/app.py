from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt, requests, tensorflow, subprocess, json

app = Flask(__name__)
api = Api(app)
client = MongoClient('mongodb://db:27017')
db = client.ImageRecognition
users = db['users']

def userExists(user):

    if users.find({'Username':user}).count() == 0:  
        return False
    return True

def verifyPassword(user, pswd):
    
    if not userExists(user):
        return False
    hashedPswd = users.find({'Username':user})[0]['Password']
    if bcrypt.hashpw(pswd.encode('utf-8'), hashedPswd) == hashedPswd:
        return True
    return False

def generateRetMap(status, msg):
    
    retMap = {
        'Status': status,
        'Message': msg
    }
    return retMap

def verifyCreds(user, pswd):
    
    if not userExists(user):
        return generateRetMap(301, 'Invalid username'), True
    correctPswd = verifyPassword(user, pswd)
    if not correctPswd:
        return generateRetMap(302, 'Invalid password'), True
    return None, False

class Register(Resource):

    def post(self):
        
        postData = request.get_json(force=True)
        if 'Username' not in postData or 'Password' not in postData:
            return jsonify(generateRetMap(301, 'Invalid username or password'))

        username = postData['Username']
        password = postData['Password']
        if userExists(username):
            return jsonify(generateRetMap(301, 'User already exists'))

        hashedPswd = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        users.insert({'Username':username,'Password':hashedPswd,'Tokens':5})
        return jsonify(generateRetMap(200, 'Registration successful'))

class Classify(Resource):
    
    def post(self):
        
        postData = request.get_json(force=True)
        if 'Username' not in postData or 'Password' not in postData:
            return jsonify(generateRetMap(301, 'Invalid username or password'))

        username = postData['Username']
        password = postData['Password']
        url = postData['URL']
        correctPswd = verifyPassword(username, password)
        if not correctPswd:
            return jsonify(generateRetMap(301, 'Invalid password'))
        
        numTokens = users.find({'Username':username})[0]['Tokens']
        if numTokens <= 0:
            return jsonify(generateRetMap(303, 'Not enough Tokens'))

        req = requests.get(url)
        retMap = {}
        with open('temp.jpg', 'wb') as fh:
            fh.write(req.content)
            proc = subprocess.Popen('python classify_image.py --model_dir=. --image_file=./temp.jpg')
            proc.communicate()[0]
            proc.wait()
            with open('text.txt') as g:
                retMap = json.load(g)

            users.update({'Username':username}, {'$set':{'Tokens':numTokens-1}})
            return jsonify(retMap)

class Refill(Resource):

    def post(self):
        
        postData = request.get_json(force=True)
        if 'Username' not in postData or 'Password' not in postData:
            return jsonify(generateRetMap(301, 'Invalid username or password'))

        username = postData['Username']
        password = postData['Password']
        tokenAmount = postData['Amount']
        correctPswd = verifyPassword(username, password)
        if not correctPswd:
            return jsonify(generateRetMap(301, 'Invalid password'))

        currTokens = users.find({'Username':username})[0]['Tokens']
        users.update({'Username':username},{'$set':{'Tokens':tokenAmount+currTokens}})
        return jsonify(generateRetMap(200, 'Tokens Refilled'))

api.add_resource(Register, '/register')
api.add_resource(Classify, '/classify')
api.add_resource(Refill, '/refill')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
