import re
import random
import time
from entities import player
from items import *


skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
			  'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
			  'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
			  'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
			  'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
			  'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
			  'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
			  'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
			  'wish', 'with', 'would']


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

	iwords = [] 

	iwords = re.sub(r"[^\w]", " ",  noPunct).split()
	
	iwords = filterWords(iwords, skip_words)
	
	return iwords

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
		print("You fall to your knees in prayer, petitioning the gods for aid... Four apples, five grapes, no bananas and one pear") 
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


def execute_take(item_id):
	"""This function takes an item_id as an argument and moves this item from the
	list of items in the current room to the player's inventory. However, if
	there is no such item in the room, this function prints
	"You cannot take that."
	"""
	taken = False

	for i in current_room["items"]:
		
		global maxWeight
		global carryWeight
		
		prospectWeight = carryWeight + i["mass"]
		
		if prospectWeight > maxWeight:
			canTake = False
		else:
			canTake = True
		
		if item_id == i["id"] and canTake == True :
			store = i
			current_room["items"].remove(i)
			player["inventory"].append(store)
			taken = True
			carryWeight = prospectWeight
			
	if taken == False:
		print()
		print("You cannot take that")

def execute_drop(item_id):
	"""This function takes an item_id as an argument and moves this item from the
	player's inventory to list of items in the current room. However, if there is
	no such item in the inventory, this function prints "You cannot drop that."
	"""
	
	global carryWeight
	
	
	dropped = False
	for i in player["inventory"]:
		if item_id == i["id"]:
			store = i
			player["inventory"].remove(i)
			current_room["items"].append(store)
			dropped = True
			carryWeight -= i["mass"]
			
	
	if dropped == False:
		print()
		print("You cannot drop that")
		
		
		
		
def execute_go(direction):
	"""This function, given the direction (e.g. "south") updates the current room
	to reflect the movement of the player if the direction is a valid exit
	(and prints the name of the room into which the player is
	moving). Otherwise, it prints "You cannot go there."
	"""
	global current_room
	
	if is_valid_exit(current_room["exits"], direction):
		current_room = rooms[currentRoom]["exits"][direction]
	else:
		print("No, You cannot go there")
		
def execute_swim():
	"""Joke function . If the player has sufficient wisdom they will realize its a bad idea and lose a wisdom point. If they aren't wise enough they go into the sea and die. """
	
	
	
	if player["WIS"] >= 7: 
		print("You realize that this probably isn't a good idea and stop once the water reaches about knee height. ")
		player["WIS"] -= 1
	else:
		print("You throw yourself into the sea and manage to flail around enough to reach deeper water. The sea gets suddenly rough and your flailing is now insufficient to keep your head above water, no matter how hard you thrash. It isn't long before you weaken and the sea swallows you for a final time." 
		)
		
def execute_kill():
	
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
	else:
		print("You consider your situation long and hard, before deciding that you will keep going. Until an end. ")
		
def execute_shout():
	"""A utility function , used to open the way to the cyclops lair"""
	
	global currentRoom
	
	print("You yell as loud as you can, the reverberation of the echoes making the illusion that entire empire has just shouted.  ")
	
	if currentRoom == rooms["cyclopsEntrance"]:
		print("You don't hear as much as you feel the cyclops rise from his slumber and heft several large heavy bars that previously prevented the door from functioning. ")
	else:
		print("despite the volume of your cry, nothing seems to react to it. ")
		
def hermes():
	
	global currentRoom
	
	if player["WIS"] in range(1,4):
		print(currentRoom["lowHelp"])
	elif player["WIS"] in range(4, 8):
		print(currentRoom["midHelp"])
	else:
		print(currentRoom["highHelp"])
		
def save():
	
	global currentRoom
	print(currentRoom)
	file = open("userData.txt", "w")
	for key in player:
		file.write(key + " " +  str(player[key]) + "\n")
	
	for key in currentRoom:
		file.write(key + " " + str(currentRoom[key])) + "\n"
	file.close()
	
def load():
	global currentRoom
	file = open("userData.txt", "r")
	for line in file:
		line.strip()
		print(line)
	
		

	
  
	