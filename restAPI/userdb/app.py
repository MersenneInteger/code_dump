from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import os, bcrypt

app = Flask(__name__)
api = Api(app)
client = MongoClient('mongodb://db:27017')
db = client.UserDB
users = db['Users']

def verifyPswd(usr, pswd):

    hashedPswd = users.find({'Username': usr})[0]['Password']
    if bcrypt.hashpw(pswd.encode('utf8'), hashedPswd) == hashedPswd:
        return True
    else: return False

def countTokens(usr):
    
    tokens = users.find({'Username': usr})[0]['Tokens']
    return tokens

def authUser(data, usr, pswd):
    pass

class Register(Resource):

    def post(self):
        
        postData = request.get_json(force=True)
        if 'Username' in postData and 'Password' in postData:
            userName = postData['Username']
            password = postData['Password']
        else:
            retMap = {
                'Status': 301,
                'Message': 'Registration Failed: Username or password missing'
            }
            return jsonify(retMap)
        
        hashedPswd = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        users.insert({
            'Username': userName,
            'Password': hashedPswd,
            'Post':'',
            'Tokens': 5
        })
        retMap = {
            'Status': 200,
            'Message': 'Registration successful'
        }
        return jsonify(retMap)

class Store(Resource):

    def post(self):
        
        postData = request.get_json(force=True)
        if 'Username' in postData and 'Password' in postData:
            userName = postData['Username']
            password = postData['Password']
            post = postData['Post']
        else:
            retMap = {
                'Status': 302,
                'Message': 'Registration Failed: Username or password missing'
            }
            return jsonify(retMap)
        correctPswd = verifyPswd(userName, password)
        if not correctPswd:
            retMap = {
                'Status': 302,
                'Message': 'Username and/or password incorrect'
            }
            return jsonify(retMap)
        numOfTokens = countTokens(userName)
        if numOfTokens <= 0:
            retMap = {
                'Status': 301,
                'Message': 'Out of tokens'
            }
            return jsonify(retMap)
        users.update({'Username': userName}, 
                     {'$set':{
                        'Post': post, 
                        'Tokens': numOfTokens-1
                        }
                     })
        retMap = {
            'Status': 200,
            'Message': 'Post successful'
        }
        return jsonify(retMap)

class Retreive(Resource):

    def post(self):
        
        postData = request.get_json(force=True)
        if 'Username' in postData and 'Password' in postData:
            userName = postData['Username']
            password = postData['Password']
        else:
            retMap = {
                'Status': 302,
                'Message': 'Registration Failed: Username or password missing'
            }
            return jsonify(retMap)

        correctPswd = verifyPswd(userName, password)
        if not correctPswd:
            retMap = {
                'Status': 302,
                'Message': 'Username and/or password incorrect'
            }
            return jsonify(retMap)

        numOfTokens = countTokens(userName)
        if numOfTokens <= 0:
            retMap = {
                'Status': 301,
                'Message': 'Out of tokens'
            }
            return jsonify(retMap)

        users.update({'Username':userName},{'$set':{'Tokens':numOfTokens-1}})
        post = users.find({'Username':userName})[0]['Post']
        retMap = {
            'Status': 200,
            'Message': post
        }
        return jsonify(retMap)

api.add_resource(Register, '/register')
api.add_resource(Store, '/store')
api.add_resource(Retreive, '/retreive')

if __name__ == "__main__":
    app.run(host='0.0.0.0')

