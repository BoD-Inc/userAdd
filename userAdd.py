import json
import boto3

def lambda_handler(event, context):
    name = str(event['body'].get('name'))
    email = str(event['body'].get('email'))
    phoneNumber = str(event['body'].get('phoneNumber'))
    auth0_id = str(event['body'].get('auth0_id'))
    newUser = "name: " + name + "\temail: " + email + "\tphone number: " + phoneNumber + "\t auth0_id: " + auth0_id
    print("New user info recievied")
    print(newUser)
    client = boto3.resource('dynamodb')
    table = client.Table("users")
    table.put_item(Item={'email':email,'name':name,'phoneNumber':phoneNumber,'auth0_id':auth0_id})