from items import *
from entities import *

""" This handles room definitions . A room is a dictionary with the following attributes 

    Name - string 
    Description - String 
    Items - list of dictionaries 
    Creatures - list of dictionaries
    Examine Description - String
    lowHelp - String - the Low WIS hint
    midHelp - String - the mid WIS hint
    highHelp - String - the high WIS hint

"""

calypsoCave={
    
    "name" : """Calypso's cave""",
    "description": "PLACEHOLDER STRING"

}
    
beach={
    
    "name" : """Calypso's island""",
    "description": "PLACEHOLDER STRING"

}
    
basement={
    
    "name" : "The Basement",
    "description": "PLACEHOLDER STRING"

}
    
    
Circe={
    
    "name" : """Circe's island""",
    "description": "You reach a beautiful island were the witch Circe is living.Circe can turn men into pigs and to protect yourself from her enchantments you can eat her magic herbs" # show, don't tell. 

}
    
treasury={
    
    "name" : "Circe's Treasury",
    "description": "PLACEHOLDER STRING"

}

    

cyclopsEntrance = {

    "name" : "Professor Poly's office",      #####??/???/???????//~?????/////??/??/?/??/?
    "description": "Up a short flight of stairs,' Professor Polyphemus's Office ' reads on a semi-translucent door in bold black letters with gold trimming. """, #this needs fixing with regard to encompassed
        
        ## examine function should print(The top of the doorway seems to be worn, perhaps by some unintentional headbutting. The door looks like you could open it if you so decide')
        ####   "items":"something to awaken the poly...? "
    
"examineDescription": "PLACEHOLDER STRING"
}

cyclops = {
    
    "name": "Cave of the Cyclops",
        
    "description": """You enter a fluorescently lit office. Aggresive clouds of whiskey vapor arrest your sense of smell water your eyes.
        In the center of the room is a large oak desk with hiking pole leaning on it.

        
        The figure slumped slumbering behind it is a broad shouldered, deepcheasted, stronglimbed, freelyfreckeled, wide mouthed, longheaded, bearkneed, brawnyhanded, ruddyfaced drunkard.
        An eyepatch clings to his skin, inset into his gaping cavernous eyesocket.
        The lofty walls of the office pulse rythmically, rumbling in time with the rise and fall of Poly's chest""",
        
    "items": [umbrella, earbuds, dinghy],
        
    "creatures" : [cyclops],                                              ##### add wake up squince
"examineDescription": "PLACEHOLDER STRING"
}

sirenCorridor = {
    "name": "The Long Corridor",
        
    "description": "The relentless Cardiffian rain has flooded the corridor. You see two men (one of which is oddly wearing ear muffs) steal your raft although your glad to part with it, they trying to    ",
    #potential for sign language further hints at absence of sound
        
    "items": [],
        
    "creatures" : [],
    
    "examineDescription":  "PLACEHOLDER STRING"

}

sirenLair = {

    "examineDescription": "PLACEHOLDER STRING"

}

rooms = {
   "calypsoCave" : calypsoCave,
   "beach" : beach,
   "basement" : basement,
   "cyclopsEntrance" :cyclopsEntrance,
   "cyclops": cyclops,
   "sirenCorridor":sirenCorridor,
   "sirenLair" :sirenLair,
   "treasury" :treasury,
   "Circe" : Circe
    }


""" This handles room definitions . A room is a dictionary with the following attributes 

    Name - string 
    Description - String 
    Items - list of dictionaries 
    Creatures - list of dictionaries
    Examine Description - String

"""
