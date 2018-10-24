from entities import player 

def save():
    global currentRoom
    file = open("userData.txt", "w")
    for key in player:
        file.write(key + " " +  str(player[key]) + "\n")