import awsgi
import json

from flask_cors import CORS
from flask import Flask, jsonify, request

from service import ddb_service
from model.Client import Client

app = Flask(__name__)
CORS(app)

BASE_ROUTE = "/client"

@app.route(BASE_ROUTE + '/<id_number>', methods=['GET'])
def get_client(id_number):
    return jsonify(ddb_service.get_client(id_number))

@app.route(BASE_ROUTE, methods=['POST'])
def create_client():
    req_json = request.get_json()

    new_client = Client(
        id_number=req_json['id_number'],
        last_name=req_json['last_name'],
        first_name=req_json['first_name'],
        country=req_json['country'],
        city=req_json['city'],
        zip_code=req_json['zip_code']
    )
    ddb_service.create_client(new_client)
    return req_json

@app.route(BASE_ROUTE, methods=['PUT'])
def update_client():
    req_json = request.get_json()

    old_client = ddb_service.get_client(req_json['id_number'])

    client_to_update = Client(
        id_number=old_client['id_number'],
        last_name=req_json['last_name'],
        first_name=req_json['first_name'],
        country=req_json['country'],
        city=req_json['city'],
        zip_code=req_json['zip_code']
    )
    ddb_service.update_client(client_to_update)
    return req_json

@app.route(BASE_ROUTE + '/<id_number>', methods=['DELETE'])
def delete_client(id_number):
    ddb_service.delete_client(id_number)
    return jsonify({"Message": f"User {id_number} deleted successfully"})

def handler(event, context):
    return awsgi.response(app, event, context)

