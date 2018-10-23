from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)
api = Api(app)
client = MongoClient('mongodb://db:27017')
db = client.BankAPI
users = db['Users']

def userExists(user):

    if users.find({'Username':user}).count() == 0:
        return False
    return True

def verifyPassword(user, passwd):

    if not userExists(user):
        return False
    hashedPswd = users.find({'Username':user})[0]['Password']
    if bcrypt.hashpw(passwd.encode('utf-8'), hashedPswd) == hashedPswd:
        return True
    return False

def getCurrentBalance(user):
    
    balance = users.find({'Username':user})[0]['Own']
    return balance

def getCurrentDebt(user):
    
    debt = users.find({'Username':user})[0]['Debt']
    return debt

def generateRetMap(status, msg):

    retMap = {
        'Status': status,
        'Message': msg
    }
    return retMap

def verifyCreds(user, passwd):
    
    if not userExists(user):
        return (generateRetMap(301, 'Username invalid'), True)
    correctPswd = verifyPassword(user, passwd)
    if not correctPswd:
        return (generateRetMap(302, 'Password invalid'), True)
    return (None, False)

def updateBalance(user, balance):
    
    users.update({'Username':user},{'$set':{'Own':balance}})

def updateDebt(user, debt):

    users.update({'Username':user},{'$set':{'Debt':debt}})

class Register(Resource):

    def post(self):
        
        postData = request.get_json(force=True)
        if 'Username' not in postData or 'Password' not in postData:
            return jsonify(generateRetMap(301, 'Username or password missing'))
        username = postData['Username']
        password = postData['Password']
        if userExists(username):
            return jsonify(generateRetMap(301, 'Invalide username'))

        hashedPswd = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        users.insert({'Username':username, 'Password':hashedPswd,'Own':0,'Debt':0})
        return jsonify(generateRetMap(200, 'Registration successful'))

class Add(Resource):

    def post(self):
        
        postData = request.get_json(force=True)
        if 'Username' not in postData or 'Password' not in postData:
            return jsonify(generateRetMap(301, 'Username or password missing'))
        username = postData['Username']
        password = postData['Password']
        amount = postData['Amount']
        retMap, err = verifyCreds(username, password)
        if err:
            return jsonify(retMap)
        
        if amount <= 0:
            return jsonify(generateRetMap(304, 'Invalid deposit amount'))
        cash = getCurrentBalance(username)
        amount -= 1
        updateBalance(username, cash + amount)
        return jsonify(generateRetMap(200, 'Deposit successful'))

class Withdraw(Resource):
    
    def post(self):
        
        postData = request.get_json(force=True)
        if 'Username' not in postData or 'Password' not in postData:
            return jsonify(generateRetMap(301, 'Username or password missing'))
        username = postData['Username']
        password = postData['Password']
        amount = postData['Amount']
        retMap, err = verifyCreds(username, password)
        if err:
            return jsonify(retMap)

        currBalance = getCurrentBalance(username)
        newBalance = currBalance - amount
        if currBalance <= 0 or newBalance < 0:
            return jsonify(generateRetMap(304,'Not enough money to complete transaction'))
        updateBalance(username, newBalance)
        return jsonify(generateRetMap(200, 'Withdraw successful'))

class CheckBalance(Resource):
    
    def post(self):

        postData = request.get_json(force=True)
        if 'Username' not in postData or 'Password' not in postData:
            return jsonify(generateRetMap(301, 'Username or password missing'))
        username = postData['Username']
        password = postData['Password']
        retMap, err = verifyCreds(username, password)
        if err:
            return jsonify(retMap)

        retMap = users.find({'Username':username},{'Password':0,'_id':0})[0]
        return jsonify(retMap)

class TakeLoan(Resource):

    def post(self):
        
        postData = request.get_json(force=True)
        if 'Username' not in postData or 'Password' not in postData:
            return jsonify(generateRetMap(301, 'Username or password missing'))
        username = postData['Username']
        password = postData['Password']
        amount = postData['Amount']
        retMap, err = verifyCreds(username, password)
        if err:
            return jsonify(retMap)
        
        currBalance = getCurrentBalance(username)
        debt = getCurrentDebt(username)
        updateBalance(username, amount + currBalance)
        updateDebt(username, debt + amount)
        return jsonify(generateRetMap(200, 'Loan successfully taken'))

class PayLoan(Resource):
    
    def post(self):

        postData = request.get_json(force=True)
        if 'Username' not in postData or 'Password' not in postData:
            return jsonify(generateRetMap(301, 'Username or password missing'))
        username = postData['Username']
        password = postData['Password']
        amount = postData['Amount']
        retMap, err = verifyCreds(username, password)
        if err:
            return jsonify(retMap)

        currBalance = getCurrentBalance(username)
        currDebt = getCurrentDebt(username)
        if currBalance < amount:
            return jsonfiy(generateRetMap(303, 'Not enough money in account'))
        if currDebt == 0:
            return jsonify(generateRetMap(303, 'No debt owed'))

        updateBalance(username, currBalance - amount)
        updateDebt(username, currDebt - amount)
        return jsonify(generateRetMap(200, 'Loan payment accepted'))
        
api.add_resource(Register, '/register')
api.add_resource(Add, '/add')
api.add_resource(Withdraw, '/withdraw')
api.add_resource(CheckBalance, '/checkbalance')
api.add_resource(TakeLoan, '/takeloan')
api.add_resource(PayLoan, '/payloan')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
