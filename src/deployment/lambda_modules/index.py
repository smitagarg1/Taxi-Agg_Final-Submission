import requests
import json
def handler(event, context):
    response = requests.get("https://reqres.in/api/users?page=2")
    print(response.text)
    print("=======================================================")
    print(json.dumps(event))
    print("=======================================================")
    #method = event.httpMethod
    #resource = event.resource
    message = json.dumps(event)
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(
                {'message': {
                    "resource": event['resource'],
                    "method": event['httpMethod'],
                    "body": event['body']
                }}
        ),
        "isBase64Encoded": False
    }