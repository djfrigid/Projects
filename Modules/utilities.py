import re
import random
from items import *
from entities import *
from rooms import *
from combat import combat
currentRoom = rooms["calypsoCave"]
shouted = False
import time

skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would']


def lockbox():
    
    global currentRoom
    
    if currentRoom == rooms["treasury"]:
        print("You kneel before the lockbox, stroking the dials with a finger. If you know the code , you might plunder it.")
        code = input("Enter the code: ")
        if code == "0451":
            print("As you dial the last number in, the lid of the box pops open slightly. You lift the lid the rest of the way, and take the item nestled in the foam.")
            player["inventory"].append(itemList["bow"])
        else:
            print("That isn't the correct code, and the locking pawls stay in place")


def checkBuffs():
    
    ranRing = False
    ranBow = False
    
    if itemList["ring"] in player["inventory"] and ranRing == False:
        player["DEX"] += 2
    
    if itemList["bow"] in player["inventory"] and ranBow == False:
        player["STR"] += 5
        


def filterWords(words, skipWords):

    for j in range (0, len(skipWords), +1):
        for i in range (0, len(words), +1):
            if words[i] == skipWords[j]:
                del words[i]
                break

    return words


def makeSense(text):

    return re.sub(r"[^a-zA-Z ]", "", text)


def normaliseInput(userInput):

    noPunct = makeSense(userInput).lower()

    rwords = re.sub(r"[^\w]", " ",  noPunct).split()
    
    qwords = filterWords(rwords, skip_words)
    
    return qwords

def questions(room):
    
    answer = input("What is your answer brave hero? (Clue: its one word) ")
    
    answer = normaliseInput(answer)
    
    if answer[0] == "red" and itemList["integrity"] not in player["inventory"]:
        print("""    Penelope Embraces you in her loving arms and your long journey has come to an end. You have 
    been dreaming of this moment for at least 20 minuet’s and you recollect every episode in your mind, every triumph 
    and every loss.  Some people might think you have changed but you are unsure, to yourself you have remained true 
    to your wife you have remained faithful. This story of you going to your lecture hall will be sung for centuries 
    if not a millennium to come and you will have solidified you place in history up there with the great Alexander, 
    and many a heroes and heroines of history, Cuchulin, Conn of hundred battles, Niall of nine hostages, Brian of 
    Kincora, the ardri Malachi, Art MacMurragh, Shane O'Neill, Major Tom, Father John Murphy, Don Quixote, Luke Skywalker, 
    Christopher Columbus, , the Mother of the Maccabees, Michal Finnigan, the Last of the Mohicans, the Rose of Castile, 
    the Man for Galway, The Man that Broke the Bank at Monte Carlo, The Man in the Gap, The Woman Who Didn't, Benjamin 
    Franklin, Napoleon Bonaparte, John L. Sullivan, Cleopatra, Savourneen Deelish, Donatello, Michelangelo, Raphael, 
    Leonardo, Splinter, Mr Rat, Pro Kirill, Julius Caesar, Paracelsus, sir Thomas Lipton, William Tell, Muhammad, Oliver 
    Stoch, the Bride of Lammermoor,  Peter the Hermit, Sgt Pepper, Peter the Packer, Queen of Hearts, Dark Rosaleen, Patrick 
    W. Shakespeare, Brian Confucius, Murtagh Gutenberg, Confucius, Patricio Velasquez, Captain Nemo, Tristan and Isolde, the 
    first Prince of Wales, Thomas Cook and Son, Soldier Boy, Arrah na Pogue, Dick Turpin, Santa and Mrs S.Grey. 
    
    Your body and mind drained, you decide to take another one of those pills before you come down and begin your journey to 
    your next class. 
    
    Penelope notices Don’t Have Much integrity left and asks you “Why did you have to use so much of that help function you 
    stupid mongrel, loser, idiot, air head?” She asks.
    “Well I didn’t know what to do! The stupid idiots that wrote game totally exaggerated the length and complexity of a game 
    although the presentation was only 20 minutes and they had all already passed their module.  I mean first I had to take the...” 
    “Oh do shut up you crazy lover boy!” She says interrupting you and kissing on you on the forehead. 
    “Well listen here Penelope, if had a pretty bad day as it is, telling me to shut up is not very nice at all”
    “I’m sorry babe how about a Chinese?”
    “No I think I’d better sit down I’m not feeling to well”
    “Ok babe”

""")
        
        time.sleep(5)
        print("Why are you still reading this?")
        time.sleep(3)
        
        print("That’s it.")
        time.sleep(3)
        
        print("The game is over")
        time.sleep(3)
        
        print("Go hope already.")
        time.sleep(5)
        print("No really there is no more.")
        time.sleep(5)
        print("just go outside and do something productive and healthy.")
        time.sleep(5)
        print("Go…")
        time.sleep(5)
        print("Ok now its over.")
        exit()

    elif answer[0] == "red" and itemList["integrity"] in player["inventory"]:
        print("""    Penelope Embraces you in her loving arms and your long journey has come to an end. 
            You have been dreaming of this moment for at least 20 minuet’s and you recollect every episode in your mind,
            every triumph and every loss.  
            Some people might think you have changed but you are unsure, to yourself you have remained true to your wife.
            This story of you going to your lecture hall will be sung for centuries if not a millennium to come and you 
            will have solidified you place in history up there with the great Alexander, and many a heroes and heroines 
            of history, Cuchulin, Conn of hundred battles, Niall of nine hostages, Brian of Kincora, the ardri Malachi, 
            Art MacMurragh, Shane O'Neill, Major Tom, Father John Murphy, Don Quixote, Luke Skywalker, Christopher Columbus, 
            the Mother of the Maccabees, Michal Finnigan, the Last of the Mohicans, the Rose of Castile, the Man for Galway, 
            The Man that Broke the Bank at Monte Carlo, The Man in the Gap, The Woman Who Didn't, Benjamin Franklin, Napoleon 
            Bonaparte, John L. Sullivan, Cleopatra, Savourneen Deelish, Donatello, Michelangelo, Raphael, Leonardo, Splinter, 
            Mr Rat, Pro Kirill, Julius Caesar, Paracelsus, sir Thomas Lipton, William Tell, Muhammad, Oliver Stoch, the Bride 
            of Lammermoor,  Peter the Hermit, Sgt Pepper, Peter the Packer, Queen of Hearts, Dark Rosaleen, Patrick W. 
            Shakespeare, Brian Confucius, Murtagh Gutenberg, Confucius, Patricio Velasquez, Captain Nemo, Tristan and Isolde, 
            the first Prince of Wales, Thomas Cook and Son, Soldier Boy, Arrah na Pogue, Dick Turpin, Santa and Mrs S.Grey. 
            
            Your body and mind drained, you decide to take another one of those pills before you come down and begin your journey 
            to your next class.  """)
        exit()
        
    else:
        room = rooms["circe"]
        print(room["name"].upper())
        print()
        print(room["description"])
        return room
        

def divineIntervention(): #this as present can be abused , consider adding a penalty
    prayer = random.randint(0,100)

    if prayer in range(0,51):
        print("You fall to your knees in prayer, petitioning the gods for aid... They ignore you.")
    elif prayer in range(51,56):
        print("You fall to your knees in prayer, petitioning the gods for aid... you are answered ")
        player["CON"] = player["MAXCON"]
    elif prayer in range(56,61):
        print("δεν μπορείτε να διαβάσετε αυτό το ... εκτός αν υποθέτω ο Έλληνας σας. Ωστόσο, αν μπορείτε, κρατήστε αυτό για τον εαυτό σας.")
    elif prayer in range(61,66):
        print("You fall to your knees in prayer, petitioning the gods for aid... No apples, four grapes, five bananas and one pear") 
    elif prayer in range(66,71):
        print("You fall to your knees in prayer, petitioning the gods for aid... Realisation that the cyclops is a liar dawns upon you.") #joke -mu
    elif prayer in range(71,76):
        print("You fall to your knees in prayer, petitioning the gods for aid... Your pocket grows strangely heavy and starts wriggling, emitting a slew of eey-ooh's. ") #joke -joke item
        player["inventory"].append(ass)
    elif prayer in range(76,81):
        print("The blurred image of the woman you love appears before you. , ")#joke - visual appealing - woman 'Ithica'
        print("""
         ......................$$I:?.............
         .....................B:....~............
         ....................$I~..T,I+...........
         ....................OIT?....+...........
         ....................TB==I...~...........
         ...................:?NI=I:,,=,..........
         ...................:+D$T?~+T?...........
         ..................,I?+O==,:$:,..........
         .................:IT?Z?::,,.~IO,,.......
         ...........,..,,=:IT+IT?.,.=,.,,.,.,....
         .............,,=++?TI??+..~.,,,,,,,,,,,,
         ,.,,.......,..,?$TII?Z?::,,,,,.,,,,,,,,,
         ,,,,..,...,,,,,?I$?I=T?:~~,,,,,,~~,,,,,,
         ,,,,,,,,,,,,,,,IT$?$IT?::~:,,,,,~~:,,,,,
            """)
    elif prayer in range(81,86):
        
        d2 = random.randint(0,2)
        if d2 == 0:
            print("You fall to your knees in prayer, petitioning the gods for aid... A sudden jolt of energy strikes through you and you feel as if you have reached a new plateau.")# insert flavourtext here
            player["CON"] += 2
        else:
            print("You fall to your knees in prayer, petitioning the gods for aid... You suddenly feel exahusted and more vulnerable.")
            player["CON"] -= 1
            
    elif prayer in range(86,91):
        print("You fall to your knees in prayer, petitioning the gods for aid... You feel refreshed as a wave of calmness washes over you.") 
        player["STA"] += 2
    elif prayer in range(91,96):
        print("You fall to your knees in prayer, petitioning the gods for aid... Your prayer is answered, your mind filling with forbidden knowledge.") #useful - restores some hints
        player["WIS"] += 1
    elif prayer in range(96,101):
        print("You fall to your knees in prayer, petitioning the gods for aid... and your prayers are answered. You feel a warm energy suffuse through your body before it turns blindingly hot and you are burned to a cinder by divine power ")
        exit()
#death


def executeTake(item):
    """This function takes an item as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    
    if item not in itemList:
        print("You cannot take that.")
    else:
        cur_item = itemList[item]
        if cur_item not in currentRoom['items']:
            print("You cannot take that.")
        else:
            player["inventory"].append(cur_item)
            print("You have taken " + cur_item["name"])
            currentRoom['items'].remove(cur_item)
    
        
def executeDrop(item):
    
    """This function takes an item as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    
    if item not in itemList:
        print("You cannot drop that.")
    else:
        cur_item = itemList[item]
        if cur_item not in player["inventory"]:
            print("You cannot drop that.")
        else:
            print("You have dropped " + cur_item['name'])
            currentRoom['items'].append(cur_item)
            player["inventory"].remove(cur_item)
    
   
def isValidExit(exits, exitChoice):
    
    return exitChoice in exits     

def printRoom():
    
    global currentRoom
        
    name = currentRoom["name"].upper()
    if name == "BLACKHOLE" or name == "REDHOLE" or name == "BLUEHOLE":
        name = ""
    else:
        print()
        description = currentRoom["description"]
        print(name.upper())
        print()
        print(description)
        
def executeGo(direction):
    
    """This function, given
    the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
   
    global currentRoom
    foughtBox = False
    foughtSiren = False 
    foughtCyclops = False
    
    if isValidExit(currentRoom["exits"], direction):
        rooms["calypsoCave"]["exits"] = {'east':'bluehole','down':'basement','north':'sirenCorridor','south':'beach'}
        currentRoom = rooms[currentRoom["exits"][direction]]
        printRoom()
        print()
        if currentRoom == rooms["basement"] and foughtBox == False:
            combat(box)
           # combatBox = True
        elif currentRoom == rooms["sirenLair"] and foughtSiren == False:
            combat(siren)
            foughtSiren = True
        elif currentRoom == rooms["bluehole"] and itemList["dinghy"] not in player["inventory"]:
            print("You have not built a raft to go there.")
            executeGo('west')
        elif currentRoom == rooms["bluehole"] and itemList["dinghy"] in player["inventory"]:
            executeGo('east')
        elif currentRoom == rooms["redhole"] and itemList["panacea"] not in rooms["cyclops"]["items"]:
            print("You have not put the panacea in the Cyclops' Cave.")
            executeGo('south')
        elif currentRoom == rooms["redhole"] and itemList["panacea"] in rooms["cyclops"]["items"]:
            executeGo('north')
        elif currentRoom == rooms["blackhole"] and itemList["earplug"] not in player["inventory"]:
            executeGo('west')
        elif currentRoom == rooms["blackhole"] and itemList["earplug"] in player["inventory"]:
            executeGo('north')
        elif foughtCyclops == False and currentRoom == rooms["cyclops"]:
            combat(monsters["cyclops"])
            foughtCyclops = True
        elif currentRoom == rooms["cyclopsEntrance"] and shouted == True:
            rooms["cyclopsEntrance"]["exits"] = {"west":"calypsoCave","south":"cyclops"}
        elif currentRoom == rooms["ithaca"]:
            currentRoom = questions(currentRoom)
    else:
        print("No, you cannot go there")
    
        
def executeSwim():
    """Joke function . If the player has sufficient wisdom they will realize its a bad idea and lose a wisdom point. If they aren't wise enough they go into the sea and die. """
    
    if player["WIS"] >= 7: 
        print("You realize that this probably isn't a good idea and stop once the water reaches about knee height. ")
        player["WIS"] -= 1
    else:
        print("You throw yourself into the sea and manage to flail around enough to reach deeper water. The sea gets suddenly rough and your flailing is now insufficient to keep your head above water, no matter how hard you thrash. It isn't long before you weaken and the sea swallows you for a final time." 
        )
        exit()
        
def executeKill():
    
    """Another joke function, should the player decide they don't want to continue playing and instead die"""

    print("There is still hope, or at least you think there is...")
    
    print()
    print()
    print()
    print()
    print()
    time.sleep(3)
    
    shouldKill = input("Are you sure you wish to abandon this mortal coil? (Yes/No)")
    
    if shouldKill.lower() == "yes":
        print("Your body seems to forget how to stay together and you fall apart into a heap of blood, bone and viscera")
        time.sleep(5)
        exit()
    else:
        print("You consider your situation long and hard, before deciding that you will keep going. Until an end. ")
        
        
def executeShout():
    """A utility function , used to open the way to the cyclops lair"""
    
    global currentRoom
    if currentRoom == rooms["cyclopsEntrance"]:
        print("You yell as loud as you can, the reverberation of the echoes making the illusion that entire empire has just shouted.  ")
        print("You don't hear as much as you feel the cyclops rise from his slumber and heft several large heavy bars that previously prevented the door from functioning. ")
        rooms["cyclopsEntrance"]["exits"] = {'west':'calypsoCave','south':'cyclops'}
    else:
        print("Despite the volume of your cry, nothing seems to react to it. ")
        
   
def hermes():
    
    global currentRoom
    
    if player["WIS"] in range(1,4):
        print(currentRoom["lowHelp"])
        player["WIS"]-=1
    elif player["WIS"] in range(4, 8):
        print(currentRoom["midHelp"])
        player["WIS"]-=1
    else:
        print(currentRoom["highHelp"])
        player["WIS"]-=1

def executeExamine(entity):
        
        
        global currentRoom
        if entity == "room" :
            print(currentRoom["examineDescription"])
            
            if currentRoom == rooms["treasury"]:
                lockbox()
                
            elif currentRoom == rooms["circe"]:
                player["inventory"].append(panacea)
            
        elif itemList[entity] in player["inventory"]:
            print(itemList[entity]["description"])
        else:
            print()
            
            
def executeBuild(boat):
    
    if planks and rope in player["inventory"]:
     
        player["inventory"].remove(planks)
        player["inventory"].remove(rope)
        player["inventory"].append(dinghy)
        print("With the power of your hands and mind you turn the wood and rope you have gathered into a functional, albeit crude dinghy. ")
   

    else:
        print("You can't build with that!")
    
    
"""    
def save():
    
    global currentRoom
    print(currentRoom)
    file = open("userData.txt", "w")
    for key in player:
        file.write(str(player[key]) + "\n")
    
    for key in currentRoom:
        file.write(str(currentRoom[key]) + "\n")
    file.close()
    
def load():
    LoadList = []
    global currentRoom
    file = open("userData.txt", "r")
    for line in file:
        line = re.sub(r"[\n]","",line)
        LoadList.append(line)
    print(LoadList)
    
    player["name"] = LoadList[0]
    player["STR"] = LoadList[1]
    player["DEX"] = LoadList[2]
    player["CON"] = LoadList[3]
    player["WIS"] = LoadList[4]
    player["STA"] = LoadList[5]
    player["inventory"] = LoadList[6]
    player["MAXCON"] = LoadList[7]
    if LoadList[8] == "Calypso's cave":
        currentRoom = rooms["calypsoCave"]
    elif LoadList[8] == "Calypso's island":
        currentRoom = rooms["beach"]
    elif LoadList[8] == "The Basement":
        currentRoom = rooms["basement"]
    elif LoadList[8] == "Circe's Mansion":
        currentRoom = rooms["Circe"]
    elif LoadList[8] == "Circe's Treasury":
        currentRoom = rooms["treasury"]
    elif LoadList[8] == "Professor Poly's office":
        currentRoom = rooms["cyclopsEntrance"]
    elif LoadList[8] == "Cave of the Cyclops":
        currentRoom = rooms["cyclops"]
    elif LoadList[8] == "The Long Corridor":
        currentRoom = rooms["sirenCorridor"]
    elif LoadList[8] == "Cheerleading practice room":
        currentRoom = rooms["sirenLair"] 
        
""" 
        
def inventory():
    
    print("You are currently carrying:")
    
    for key in player["inventory"]:
        print(key["name"])
        
        
def instruction():
    print("""You can:
        go - move to another room(either north, south, east, west, up, or down)
        drop - drop an item
        take - take an item
        pray - pray to the Gods
        build - build using items in your inventory
        examine - look a bit closer at a room or item
        help - Hermes will give you a hint
        shout - SHOUT!
        swim - go for a swim
        kill - sometimes life gets a bit too much
        save - save your progress
        load - load a savegame
        inventory - see what you are carrying
        stats - have a look at your current stats
        eat - consume an item in your inventory""")
    
    
def playerStats(player):
    print("STRENGTH: " + str(player["STR"]))
    print("DEXTERITY: " + str(player["DEX"]))
    print("CONSTITUTION: " + str(player["CON"]))
    print("WISDOM: " + str(player["WIS"]))
    print("STAMINA: " + str(player["STA"]))
    
def eat(item):

    if item == "sandwich":
        if itemList["sandwich"] in player["inventory"]:
            if player["CON"] >= player["MAXCON"] - 10:
                player["CON"] = player["MAXCON"]
                print("Your hp has maxed out.")
                player["inventory"].remove(sandwich)
            else:
                player["CON"] += 10
                print("You recover 10hp")
                player["inventory"].remove(sandwich)
        else:
            print("You do not have this item.")
    elif item == "drink":
        if itemList["drink"] in player["inventory"]:
            if player["CON"] >= player["MAXCON"] - 3:
                player["CON"] = player["MAXCON"]
                print("Your hp has maxed out.")
                player["inventory"].remove(drink)
            else:
                player["CON"] += 3
                print("You recover 3hp")
                player["inventory"].remove(drink)
        else:
            print("You do not have this.")
    elif item == "crisps":
        if itemList["crisps"] in player["inventory"]:
            if player["CON"] >= player["MAXCON"] - 5:
                player["CON"] = player["MAXCON"]
                print("Your hp has maxed out.")
                player["inventory"].remove(crisps)
            else:
                player["CON"] +=5
                print("You recover 5hp")
                player["inventory"].remove(crisps)
    else:
        print("You do not have this item.")
            
            
def executeCommand(command):
    
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.
    """
    
    global currentRoom
    
    if 0 == len(command):
        return

    if command[0] == "go":
        
        if len(command) > 1:
            executeGo(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        
        if len(command) > 1:
            executeTake(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        
        if len(command) > 1:
            executeDrop(command[1])
        else:
            print("Drop what?")
            
    elif command [0] == "build":
        
        if len(command) > 1:
            if command[1] =="boat":
                executeBuild(command[1])
            else:
                print("You cannot build that.")
        else:
            print("Build what?")
            
    elif command [0] == "examine":
        
        if len(command) > 1:
            executeExamine(command[1])
        else:
            print("Examine what?")
            
    elif command [0] == "shout":
        executeShout()        
        
    elif command [0] == "swim":
        executeSwim()
        
    elif command [0] == "kill":
        executeKill()
        
    elif command[0] == "pray":
        divineIntervention()
        
    elif command[0] == "help":
        hermes()

    
    elif command[0] == "inventory":
        inventory()
        
    elif command[0] == "instruction":
        instruction()
          
    elif command[0] == "stats":
        playerStats(player)
        
    elif command[0] == "eat":
        if len(command) > 1:
            eat(command[1])
    
    else:
        print("This makes no sense.")