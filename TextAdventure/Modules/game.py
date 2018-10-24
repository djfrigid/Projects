""" This file will contain the game logic and functions related to displaying information

    game name?
    
    variable naming convention. i am using this so a variable called "my variable" should be called "myVariable" and NOT "my_variable "
    

 """

from creation import *
from combat import *
from entities import *
from utilities import *
from rooms import *
import os, time

def checkCave():
    
    if raft in player["inventory"]:
        rooms["calypsoCave"]["exits"] = {
            
            'east':'cyclopsEntrance',

            'down':'basement',

            'south':'beach'}
        
    if dinghy in player["inventory"]:
        rooms["calypsoCave"]["exits"] =  {
            
            'east':'cyclopsEntrance',

            'down':'basement',

            'south':'beach',
            
            "north" : "sirenCorridor"}
        
    else:
        rooms["calypsoCave"]["exits"] = {
            
            "down" : "basement",
            "south" : "beach"
            
            }
        
        
        
def checkLair():
    
    global currentRoom
    
    if currentRoom == rooms["sirenCorridor"] and earplug not in player["inventory"]:
        currentRoom = rooms["sirenLair"]           
    
def checkExits():
    
    checkCave()
    checkLair()


def main():
    

    #os.system("start D:\Eclipse\eclipse\Repositories\TextAdventure\TextAdventure\Modules\Sound.wav")
    print('''       Out into the rain in miserable Cardiff you go, after reading an article about the amount of 
    deaths caused by pharmacy errors(1 in 1000!).
    You are hunched over with a cigarette in your mouth, it goes out seconds after it was lit after 
    a BMWx5 sped through a puddle.
    Treating yourself to Tescos' 3 pound meal deal, you arrive at the pharmacy. The slippers you 
    are wearing are visibly soaked, they squelch as you approach the counter. The woman
    behind it looks at you judgingly, visibly unimpressed, and when you ask for a box of flu medicine,
    she returns squinting at the box in her hand, seemingly unable to read it without
    her glasses. She hands you a box of 'Oddssydinazacitidine'.
       
       'POSSIBLE SIDE AFFECTS MAY INCLUDE':
        *Causing serious tranformation of reality, passing body and mind to hyperquantum capacities,
        *Magicular particles in your vicinity may double to relative inevitability,
        *Fractal dimensions above infinity+1 collapsing into a finite equilibrium.
        *Mild nausea
        *Drowsiness
        
        You take it politely without question, reasoning that 1 in 1000 is a tremendously small percentage...
        As you start the 10 minute walk back to your lectures, you pop 3 of the little yellow pills.
        Suddenly you heart starts to thump, your knees become weak...
          
    ''')
     
    print(rooms["calypsoCave"]["name"].upper())
    print()
    print(rooms["calypsoCave"]["description"])
    
    
    while True:
        
        
                    
        checkExits()
        
        action = input("> ")
        
        command = normaliseInput(action)
        
        executeCommand(command)
        
 
        
        
if __name__ == "__main__":
    main()



"""
Command List:

Move d
Drop d
Take d
Pray d
Build d
Examine - this works on rooms and items (and sorceressess) d
Help - Hermes -c
Shout 
Swim
Kill
Save
Load
Inventory



Exit objects / global variables to prevent the player using an exit before they have solved the required puzzle


Kryla (say krill-ah) - secret boss thats massively OP - reward is one letter l

time.sleep() #sleeps for a given amount of seconds 

winsound - for playing of sound files 

secret code hidden in the ascii images - unlocks a powerful single use item - code 0451

Special Conditions:

nned raft to go  to polys office

need dinghy and to go to sirenCorridor

earbuds or pull to siren lair 

shout to open cave of cyclops 




"""