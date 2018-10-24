""" This file will contain the game logic and functions related to displaying information

    game name?
    
    variable naming convention. i am using this so a variable called "my variable" should be called "myVariable" and NOT "my_variable "
    

 """

from creation import *
from combat import *
from entities import *
from utilities import *
from rooms import *


def main():
    
    
    
    while True:
        
        
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

"""