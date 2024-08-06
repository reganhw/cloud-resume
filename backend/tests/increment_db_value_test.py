import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api.cosmos_db_funcs import increment_db_value
import items

container = items.container
numbers =items.numbers
colors = items.colors

items.create_items()

for i in range (5):                                                       # For all items...
    assert increment_db_value(container, str(i), 'number')==numbers[i]+1  # Check that 'increment_db_value' returns 1 + old value.
    item = container.read_item(item = str(i), partition_key = str(i))     # Read in updated item.
    assert item['number']==numbers[i]+1                                   # Check that 'number' was correctly updated.
    assert item['color']==colors[i]                                       # Check that 'color' was unchanged.

    
items.delete_items()