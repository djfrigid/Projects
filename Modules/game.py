from creation import *
from combat import *
from entities import *
from utilities import *
from rooms import *

def checkCave():
    
    if itemList["raft"] in player["inventory"]:
        rooms["calypsoCave"]["exits"] = {
            
            'east':'cyclopsEntrance',

            'down':'basement',

            'south':'beach'}
        
    if itemList["dinghy"] in player["inventory"]:
        rooms["calypsoCave"]["exits"] = {
            
            'east':'cyclopsEntrance',

            'down':'basement',

            'south':'beach',
            
            "north" : "sirenCorridor"}
        
    else:
        rooms["calypsoCave"]["exits"] = {
            
            "down" : "basement",
            "south" : "beach"}         
    
def main():
    
    create()
     
    print(rooms["calypsoCave"]["name"].upper())
    print()
    print(rooms["calypsoCave"]["description"])
        
    while True:
                    
        checkCave()
        
        action = input("> ")
        
        command = normaliseInput(action)
        
        executeCommand(command)
        
 
        
        
if __name__ == "__main__":
    main()