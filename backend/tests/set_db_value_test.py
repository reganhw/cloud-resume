import sys,os, random
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api.cosmos_db_funcs import set_db_value
import items

container = items.container
numbers =items.numbers
colors = items.colors

items.create_items()                                                      # Create items in Test container.

new_numbers = [random.randint(1,10) for i in range (5)]                   # Five random integers.

for i in range (5):                                                       # For all items...
    set_db_value(container, str(i), 'number', new_numbers[i])             # Change 'number' value to one in 'new_numbers'.
    item = container.read_item(item = str(i), partition_key = str(i))     # Read the item.
    assert item['number']==new_numbers[i]                                 # Check that 'number' was correctly updated.
    assert item['color']==colors[i]                                       # Check that 'color' was unchanged.

    
items.delete_items()                                                      # Delete items in Test container.