import azure.functions as func, os
from azure.cosmos import CosmosClient
from cosmos_db_funcs import increment_db_value

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

# Set variables
URI = os.environ['ACCOUNT_URI']
KEY = os.environ['ACCOUNT_KEY']
client = CosmosClient(URI, credential=KEY)
DATABASE_NAME = 'CloudResume'
CONTAINER_NAME = 'VisitorCount'
ID = "01"

@app.route(route="update_visitor_count")
def update_visitor_count(req: func.HttpRequest) -> func.HttpResponse:   # HTTP Trigger function
    
    database = client.get_database_client(DATABASE_NAME)
    container = database.get_container_client(CONTAINER_NAME)

    new_count = increment_db_value(container, ID, "visitorCount")

    return func.HttpResponse(
        body = f"{new_count}", status_code=200                          # Return the new visitor count. 
    )