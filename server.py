import os
from flask import Flask, flash, request, redirect, url_for
from flask import send_from_directory, jsonify
from json import dumps
import pymongo
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
app.secret_key = 'super secret key'
cors = CORS(app)
cors = CORS(app, resources = {r"/api/*":{"origins":"*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/check', methods=['GET'])
def check():
    uname = str(request.args.get('uname'))
    passw = str(request.args.get('pass'))
    typ = str(request.args.get('type'))
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["users"]
    if typ == "student":
        cursor = mydb.student.find({"username":uname})
    else:
        cursor = mydb.teacher.find({"username":uname})
    for i in cursor:
        pas = i['password']
        print(pas, passw)
        if pas==passw:
            return jsonify("yes")
        else:
            return jsonify("no")
    return jsonify("no")

@app.route('/add', methods = ['POST'])
def add():
    model = json.loads(request.data)
    print(model)
    name = str(model["name"])
    uname = str(model["username"])
    passw = str(model["password"])
    typ = str(model["type"])
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["users"]
    if typ == "student":
        cursor = mydb.student.find({"username":uname})
    else:
        cursor = mydb.teacher.find({"username":uname})
    data = list()
    for i in cursor:
        data.append(i)
    if(len(data)>0):
        return jsonify("username exists")
    else:
        if typ == "student":
            cursor = mydb.student.insert({"username":uname, "password":passw, "name":name})
        else:
            cursor = mydb.teacher.find({"username":uname, "password":passw, "name":name})
        return jsonify("user registered!")
    # return model

if __name__=="__main__":
    app.debug = True
    app.run()