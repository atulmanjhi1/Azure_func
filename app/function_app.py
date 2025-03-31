import azure.functions as func
from api.demo import hello

app = func.FunctionApp()

app.register_blueprint(hello)
