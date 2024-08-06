# Get the visitor count from the command line
import json
from azure.cosmos import CosmosClient

# Import account uri and key.
f = open('api/local.settings.json')
data = json.load(f)
URI = data["Values"]["ACCOUNT_URI"]
KEY = data["Values"]["ACCOUNT_KEY"]
f.close()

# Set Cosmos DB values. Connect to testing container.
client = CosmosClient(URI, credential=KEY)
DATABASE_NAME = 'CloudResume'
CONTAINER_NAME = 'VisitorCount'
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

visitor_count = container.read_item(item= "01", partition_key="01")["visitorCount"]
print(visitor_count)