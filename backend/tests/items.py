# File for creating and deleting items in the Test database.
import json, random, os
from azure.cosmos import CosmosClient

# Import account uri and key.
cur_path = os.path.dirname(__file__)                             # Current path
loc = os.path.relpath('../api/local.settings.json', cur_path)    # Path to json file
f = open(loc)
data = json.load(f)
URI = data["Values"]["ACCOUNT_URI"]
KEY = data["Values"]["ACCOUNT_KEY"]
f.close()

# Set Cosmos DB values. Connect to testing container.
client = CosmosClient(URI, credential=KEY)
DATABASE_NAME = 'CloudResume'
CONTAINER_NAME = 'Test'
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

numbers = [random.randint(1,10) for i in range (5)]           # Five random integers.
colors = ["red", "blue", "green", "black", "white"]           # Five colors (strings).

def create_items():
    # Create items inside container. 

    for i in range (5):                                        # Create five items.
        container.upsert_item({
                'id': str(i),                                  # 'id' set to 0...4
                'number': numbers[i],                          # 'number' set to value in 'starting_numbers'.
                'color': colors[i]                             # 'color' set to string in 'colors'.
            }
        )
    return None;

def delete_items():
    for i in range (5):
          container.delete_item(item = str(i), partition_key = str(i))          # Delete all items.