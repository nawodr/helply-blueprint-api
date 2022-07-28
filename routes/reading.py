from flask import request, jsonify, make_response

from . import routes

from models.readingModel import getStudentList, getStudentByName


@routes.route("/", methods=['GET'])
def studentList():
    x = 1
    name = getStudentList(x)

    return name


@routes.route("/login", methods=['POST'])
def login():
    req = request.get_json()
    username = req['username']
    password = req['password']

    user = getStudentByName(username, password)
    if len(user) == 0:
        data = {
            "body": [],
            "message": "Failed"
        }
    else:
        data = {
            "body": user,
            "message": "Success"
        }

    body = jsonify(data)
    return make_response(body)


@routes.route("/get", methods=['GET'])
def getUser():
    req = request.get_json()
    username = req['username']
    password = req['password']

    user = getStudentByName(username, password)
    if user is None:
        message = jsonify(message="Failed")
    else:
        message = jsonify(message="Success")

    body = jsonify(body=user)
    return body
