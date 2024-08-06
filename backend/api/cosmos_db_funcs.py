# container: Cosmos DB container.
# id: The id of the item. It is assumed that the partition key is the id.
# key: Key in the dictionary to look up.

def get_db_value(container, id, key):
    '''
    Reads a value from cosmos DB item.
    '''
    return container.read_item(item = id, partition_key = id)[key]

def set_db_value(container, id, key, val):
    '''
    Updates a value in a cosmos DB item.
    '''
    item = container.read_item(item = id, partition_key = id)
    item[key] = val
    container.upsert_item(item)  
    return None                                    

def increment_db_value(container, id, key):
    '''
    Increments the value of a cosmos DB item.
    '''
    item = container.read_item(item = id, partition_key = id)
    current_val = item[key]
    new_val = current_val +1
    item[key] = new_val
    container.upsert_item(item)
    return new_val
