import boto3
import os

from boto3.dynamodb.types import TypeDeserializer, TypeSerializer

client = boto3.client("dynamodb")
CT_CLIENT_TABLE = os.getenv("STORAGE_CTCLIENT_NAME")

def from_dynamodb_to_json(item):
     d = TypeDeserializer()
     return {k: d.deserialize(value=v) for k, v in item.items()}

def get_client(id_number):
     item = client.get_item(TableName=CT_CLIENT_TABLE, Key={
          'id_number': {
               'S': id_number
          }
     })
     return from_dynamodb_to_json(item['Item'])

def create_client(ct_client):
     client.put_item(TableName=CT_CLIENT_TABLE, Item={
          "id_number": {
               "S": ct_client.id_number
          },
          "city": {
               "S": ct_client.city
          },
          "country": {
               "S": ct_client.country
          },
          "first_name": {
               "S": ct_client.first_name
          },
          "last_name": {
               "S": ct_client.last_name
          },
          "zip_code": {
               "N": ct_client.zip_code
          }
     })
     return ct_client

def update_client(ct_client):
     client.put_item(TableName=CT_CLIENT_TABLE, Item={
          "id_number": {
               "S": ct_client.id_number
          },
          "city": {
               "S": ct_client.city
          },
          "country": {
               "S": ct_client.country
          },
          "first_name": {
               "S": ct_client.first_name
          },
          "last_name": {
               "S": ct_client.last_name
          },
          "zip_code": {
               "N": ct_client.zip_code
          }
     })
     return ct_client

def delete_client(id_number):
     client.delete_item(TableName=CT_CLIENT_TABLE, Key={
          'id_number': {
               'S': id_number
          }
     })
     return ""