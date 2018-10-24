def eat(item):

	if item == "sandwich":
		if ItemList["sandwich"] in player["inventory"]:
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
		if ItemList["drink"] in player["inventory"]:
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
		if ItemList["crisps"] in player["inventory"]:
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

-

	elif command[0] == "eat":
		if len(command) > 1:
			eat(command[1])




-
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
		currentRoom = rooms['calypsoCave']
	elif LoadList[8] == "Calypso's island":
		currentRoom = rooms['beach']
	elif LoadList[8] == "The Basement":
		currentRoom = rooms["basement"]
	elif LoadList[8] == "Circe's Mansion":
		currentRoom = rooms["circe"]
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
	else:
		 print("You cannot load") 