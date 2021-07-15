import json
import boto3

def lambda_handler(event, context):
    name = str(event['body'].get('name'))
    email = str(event['body'].get('email'))
    phoneNumber = str(event['body'].get('phoneNumber'))
    newUser = "name: " + name + "\temail: " + email + "\tphone number: " + phoneNumber
    print("New user info recievied")
    print(newUser)
    client = boto3.resource('dynamodb')
    table = client.Table("users")
    table.put_item(Item={'email':email,'name':name,'phoneNumber':phoneNumber})