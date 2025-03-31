import azure.functions as func
import json

hello = func.Blueprint()

@hello.route(route="demo")
def demo(req: func.HttpRequest) -> func.HttpResponse:
    '''
    Simple Azure Function to return "Hello, World!" message.

    Returns:
        Hello World message in JSON format.
    '''
    try:
        response = {"message": "Hello, World!"}

        return func.HttpResponse(
            json.dumps(response),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        return func.HttpResponse(
            json.dumps({"error": str(e), "status": "failed", "statusCode": "400"}),
            status_code=400,
            mimetype="application/json"
        )
