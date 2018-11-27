from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt
import spacy

app = Flask(__name__)
api = Api(app)
client = MongoClient('mongodb://db:27017')
db = client.SimilarityDB
users = db['users']

def userExists(usr):
    
    if users.find({'Username': usr}).count() == 0:
        return False
    return True

def verifyPswd(usr, pswd):
    
    if not userExists(usr):
        return False
    hashedPswd = users.find({'Username': usr})[0]['Password']
    if bcrypt.hashpw(pswd.encode('utf-8'), hashedPswd) == hashedPswd:
        return True
    return False

def countTokens(usr):
    
    tokens = users.find({'Username':usr})[0]['Tokens']
    return tokens

def generateRetMap(status, msg):
    
    retMap = { 'Status': status,
              'Message': msg
    }
    return retMap

class Register(Resource):
    
    def post(self):
        
        postData = request.get_json(force=True)
        if 'Username' not in postData or 'Password' not in postData:
            return jsonify(generateRetMap(301, 'Username or password missing'))

        username = postData['Username']
        password = postData['Password']
        if userExists(username):
            return jsonify(generateRetMap(301, 'Invalid Username'))

        hashedPswd = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        users.insert({'Username': username, 'Password': hashedPswd, 'Tokens': 6 })
        return jsonify(generateRetMap(200, 'Registration Successful'))

class Detect(Resource):

    def post(self):
        
        postData = request.get_json(force=True)
        if 'Username' not in postData or 'Password' not in postData:
            return jsonify(generateRetMap(301, 'Username or password missing'))

        username = postData['Username']
        password = postData['Password']
        text1 = postData['Text1']
        text2 = postData['Text2']

        if not userExists(username):
            return jsonify(generateRetMap(301, 'Invalid username'))
        correctPswd = verifyPswd(username, password)
        if not correctPswd:
            return jsonify(generateRetMap(302, 'Invalid password'))

        numTokens = countTokens(username)
        if numTokens <= 0:
            return jsonify(generateRetMap(303, 'Out of tokens, please refill'))

        nlp = spacy.load('en_core_web_sm')
        text1 = nlp(text1)
        text2 = nlp(text2)
        similarityRatio = text1.similarity(text2)
        retMap = {
            'Status': 200,
            'Similarity': similarityRatio,
            'Message': 'Similarity calculated'
        }
        currTokens = countTokens(username)
        users.update({'Username': username},{'$set':{'Tokens':currTokens-1}})
        return jsonify(retMap)

class Refill(Resource):

    def post(self):
        
        postData = request.get_json(force=True)
        if 'Username' not in postData or 'Password' not in postData:
            return jsonify(generateRetMap(301, 'Username or password missing'))

        username = postData['Username']
        password = postData['Password']
        refillAmount = postData['Refill']
        if not userExists(username):
            return jsonify(generateRetMap(301, 'Invalid Username'))

        correctPswd = verifyPswd(username, password)
        if not correctPswd:
            return jsonify(generateRetMap(302, 'Invalid Password'))

        currTokens = countTokens(username)
        users.update({'Username': username},{'$set':{'Tokens':currTokens + refillAmount}})
        return jsonify(generateRetMap(200, 'Tokens successfully refilled'))
        
api.add_resource(Register, '/register')
api.add_resource(Detect, '/detect')
api.add_resource(Refill, '/refill')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

