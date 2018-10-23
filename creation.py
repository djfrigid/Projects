"""This file handles the creation of the player character at the beginning of the game """

from entities import player

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
        
        if choice == "STR":
            player["STR"] +=1
        elif choice == "DEX":
            player["DEX"]+=1
        elif choice == "WIS":
            player["WIS"]+=1
        elif choice == "STA":
            player["STA"]+=1
        elif choice == "CON":
            player["CON"]+=1
        else: 
            print("That's not an aspect of yourself, unless of course you are being a deliberate pain.You don't need to improve on that ")

    player["MAXCON"] = player["CON"]
            
#i am likely to update this so the player can assign more than one point at once and again for balancing