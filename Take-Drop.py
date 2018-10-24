def executeTake(item):
    """This function takes an item as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    
    if item not in ItemList:
        print("You cannot take that.")
    else:
        cur_item = ItemList[item]
        if cur_item not in currentRoom['items']:
            print("You cannot take that.")
        else:
            player["inventory"].append(cur_item)
            print("You have taken " + cur_item["name"])
            print("Item description: " + cur_item["description"])
            currentRoom['items'].remove(cur_item)
    
        
def executeDrop(item):
    
    """This function takes an item as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    
    if item not in ItemList:
        print("You cannot drop that.")
    else:
        cur_item = ItemList[item]
        if cur_item not in player["inventory"]:
            print("You cannot drop that.")
        else:
            print("You have dropped " + cur_item['name'])
            currentRoom['items'].append(cur_item)
            player["inventory"].remove(cur_item)