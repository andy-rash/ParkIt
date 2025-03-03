from flask import jsonify

def success(message):
    response = jsonify({"error": "success", "message": message})
    response.status_code = 200
    return response

def bad_request(message):
    response = jsonify({"error": "bad request", "message": message})
    response.status_code = 400
    return response

def unauthorized(message):
    response = jsonify({"error": "unauthorized", "message": message})
    response.status_code = 401
    return response

def forbidden(message):
    response = jsonify({"error": "forbidden", "message": message})
    response.status_code = 403
    return response
