from responses import sendResponse

def lambda_handler(event, context):
    # TODO implement
    print(event)
    todos = [
        { "id": 1, "title": "Köp kaffe", "done": False },
        { "id": 2, "title": "Köp kaka", "done": False }
    ]

    return sendResponse(200, todos)

