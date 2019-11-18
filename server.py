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

# login route
@app.route('/check', methods=['GET'])
def check():
    uname = str(request.args.get('uname'))
    passw = str(request.args.get('pass'))
    typ = str(request.args.get('type'))
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["users"]
    if typ == "Student":
        print("student")
        cursor = mydb.student.find({"username":uname})
    else:
        cursor = mydb.teacher.find({"username":uname})
    for i in cursor:
        print("1")
        pas = i['password']
        print(pas, passw)
        if pas==passw:
            return jsonify("yes")
        else:
            return jsonify("no")
    return jsonify("no")

@app.route('/username_exists', methods= ['POST'])
def username_exists():
    uname = request.data.decode(encoding="utf-8")
    print(uname)
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["users"]
    cursor1 = mydb.student.find({"username":uname})
    cursor2 = mydb.teacher.find({"username":uname})
    data = list()
    for i in cursor1:
        data.append(i)
    for i in cursor2:
        data.append(i)
    if(len(data)>0):
        print("FOUND OOPS")
        return jsonify("True")
    else:
        return jsonify("False")

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
    if typ == "Student":
        cursor = mydb.student.find({"username":uname})
    else:
        cursor = mydb.teacher.find({"username":uname})
    data = list()
    for i in cursor:
        data.append(i)
    if(len(data)>0):
        return jsonify("username exists")
    else:
        if typ == "Student":
            cursor = mydb.student.insert({"username":uname, "password":passw, "name":name})
        else:
            cursor = mydb.teacher.find({"username":uname, "password":passw, "name":name})
        return jsonify("user registered!")
    # return model

if __name__=="__main__":
    app.debug = True
    app.run()