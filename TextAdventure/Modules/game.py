""" This file will contain the game logic and functions related to displaying information

    game name?
    
    variable naming convention. i am using this so a variable called "my variable" should be called "myVariable" and NOT "my_variable "
    

 """

from creation import *
from combat import *
from entities import *
from utilities import *
from rooms import *

    

def execute_command(command):
    
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """
    
    
    if 0 == len(command):
        return

    if command[0] == "go":
        
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")
            
    elif command [0] == "build":
        
        if len(command) > 1:
            execute_build(command[1])
        else:
            print("Build what?")
            
    elif command [0] == "examine":
        
        if len(command) > 1:
            execute_examine(command[1])
        else:
            print("Examine what?")
            
    elif command [0] == "shout":
        execute_shout()        
        
    elif command [0] == "swim":
        execute_swim()
        
    elif command [0] == "kill":
        execute_kill()
        
    elif command[0] == "pray":
        divineIntervention()
        
    elif command[0] == "help":
        help()
            
    else:
        print("This makes no sense.")
        
currentRoom = rooms["beach"]
print(currentRoom)
        
save()




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



Exit objects / global variables to prevent the player using an exit before they have solved the required puzzle


Kryla (say krill-ah) - secret boss thats massively OP - reward is one letter l

time.sleep() #sleeps for a given amount of seconds 

winsound - for playing of sound files 

secret code hidden in the ascii images - unlocks a powerful single use item - code 0451

"""