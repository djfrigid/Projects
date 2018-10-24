"""This file handles the creation of the player character at the beginning of the game """

from entities import player
from rooms import *
import re

def create():
     
     
    availablePoints = 10

    while availablePoints > 0:
        
        print("You can still improve on yourself. Select one of the following to increase: " + "\n")
        print("STR(currently " + str(player["STR"]) + ") : Your physical strength will affect the amount of damage you deal in combat." + "\n")
        print("DEX(currently " + str(player["DEX"]) + ") : Your dexterity determines your odds of evading your opponents blows. " + "\n")
        print("WIS(currently " + str(player["WIS"]) + ") : Your wisdom will determine both the number and quality of hints available to you. " + "\n")
        print("STA(currently " + str(player["STA"]) + ") : Your stamina will determine the amount of special attacks you can use in combat. " + "\n")
        print("CON(currently " + str(player["CON"]) + ") : Your body's constitution will determine the amount of health you have access to. " + "\n")
        
        print("You have " + str(availablePoints) + " points left.")
        
        choice = input(">")
        
        choice = choice.upper()
        choice = choice.strip()
        choice = re.sub(r"[^STR, DEX, WIS, STA, CON]", "", choice)
        
        number = int(input("And how many points?"))
        
        canAdd = True
        
        if availablePoints - number < 0:
            print("you cannot assign that many points. You only have " + str(availablePoints) + " remaining")
            canAdd = False
            
        if canAdd == True:
              
            if choice == "STR":
                player["STR"] += number
                availablePoints -= number
            elif choice == "DEX":
                player["DEX"]+= number
                availablePoints -= number
            elif choice == "WIS":
                player["WIS"]+= number
                availablePoints -= number
            elif choice == "STA":
                player["STA"]+= number
                availablePoints -= number
            elif choice == "CON":
                player["CON"]+= number
                availablePoints -= number
            else: 
                print("That's not an aspect of yourself, unless of course you are being a deliberate pain.You don't need to improve on that ")
    
       

    player["MAXCON"] = player["CON"]        
#i am likely to update this so the player can assign more than one point at once and again for balancing