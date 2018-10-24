"""This file is for functions relating to the combat system"""

import random
from entities import *
from items import *
from rooms import rooms

def combat(monster):
    
    print(monster)
    
    
    
    if monster == monsters["cyclops"] and umbrella in player["inventory"]:
        print("You stab Poly in his eye with the tip of the umbrella. He roars in pain and collapses into a ball, cradling his ruined face.")
        monster["CON"] = 0

    while player["CON"] >= 0 and monster["CON"] >= 0 :
    
        action = input("What attack do you use, normal or special? ")
        print()
    
        if action == "normal":
            
            toHitm = random.randint(1,10) - monster["DEX"]
            
            if toHitm >= monster["DEX"]:
                
                playDamage = random.randint(1,player["STR"])
                monster["CON"] -= playDamage
                print("You deal " + str(playDamage) + " damage to the " + monster["name"] + "\n")
            
            else:
                
                print("You try and hit the " + monster["name"] + " but it dodges out of the way" + "\n")
                
            
        elif action == "special" and player["STA"] > 0 :
            
            determinant = random.randint(0,5)
            
            if determinant == 0:
                
                print("You strike your opponent in the knee and hear a satisfying crunch. They hobble clear, favouring the undamaged leg ")
                player["STA"] -= 3
                monster["DEX"] -= 1
                
            elif determinant == 1:
                
                print("You grab your opponents arm and wrench, being rewarded with the sharp crack of breaking bone. The limb hangs uselessly at their side, out of the fight")
                player["STA"] -=1
                monster["STR"]-=1
                
            elif determinant == 2:
                
                print("You jab your fingers into your opponents face , gouging deep into an eye. They twist away, leaving your fingers coated in blood and jelly... and them now half blind")
                player["STA"] -=1
                monster["DEX"]-=2
                monster["CON"]-=3
                
            elif determinant == 3:
                
                print("You throw your opponent to the ground and smash their skull down one,two,three times before you are forced away. Blood leaks from the side of their head and their eyes have a glazed over look ")
                player["STA"] -= 1
                monster["STR"] -= 1
                monster["DEX"] -= 1
                monster["CON"] -= 2
                
            elif determinant == 4:
                
                print("You hit hard into the stomach , so hard in fact your opponent doubles over vomiting, the move clearly having taken something out of them")
                player["STA"] -=1
                monster["CON"] -= random.randint(1,player["STR"])

            elif action == "special" and player["STA"] <= 0:

                print("You try a fancy move but cannot find the energy to do something beyond a normal attack ")

                toHitm = random.randint(1,10) - monster["DEX"]
            
                if toHitm >= monster["DEX"]:
                    
                    playDamage = random.randint(1,player["STR"])
                    monster["CON"] -= playDamage
                    print("You deal " + str(playDamage) + " to the " + monster["name"] + "\n")
            
                else:
                
                    print("You try and hit the " + monster["name"] + " but it dodges out of the way" + "\n")
                
        toHitp = random.randint(1,10) - player["DEX"]    
        if toHitp >= player["DEX"]:
            if monster["STR"] > 1:
                
                    enemDamage = random.randint(1,monster["STR"])        
                    player["CON"] -= enemDamage
                    print("You take " + str(enemDamage) + " damage from the " + monster["name"] + "\n")
                
            else:
                    print("You are hit, but take no damage")
        else:
            print("The " + monster["name"] + " tries to hit you, but you dodge out of the way" + "\n")
        
        if player["CON"] <=0 :
            print("---------------------------------")
            print("You are slain by the " + monster["name"] + ". Your journey is over. You failed.")
            print("---------------------------------")
            exit()
        elif monster["CON"] <= 0:
            print("---------------------------------")
            print("With a mighty blow, you defeat the " + monster["name"]) #change the flavourtext here 
            print("---------------------------------")
            
            if monsters["box"] == monster:
                print("The box shatters into pieces, several to be good sturdy planks, you take them, confident they will be of use.")
                player["inventory"].append(itemList["planks"])

                
        