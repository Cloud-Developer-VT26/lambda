import json

def sendResponse(statusCode, data):
    return {
        'statusCode': statusCode,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps(data)
    }