from items import *

""" This handles room definitions . A room is a dictionary with the following attributes 

    Name - string 
    Description - String 
    Items - list of dictionaries 
    Creatures - list of dictionaries
    Examine Description - String

"""

rooms = {
    calypsoCave,
    beach,
    basment,
    cyclopsEntrance,
    cyclops,
    sirenCorridor,
    sirenLair,
    treasury,
    Circe
    }


calypsoCave={
    
    "name" : """Calypso's cave""",
    "description": "PLACEHOLDER STRING"

}
	
beach={
    
    "name" : """Calypso's island""",
    "description": "PLACEHOLDER STRING"

}
	
basment={
    
    "name" : "The Basment",
    "description": "PLACEHOLDER STRING"

}
	
    
Circe={
    
    "name" : """Circe's island""",
    "description": "You reach a beautiful island were the witch Circe's living.Circe could turns men into pigs and to protect yourself from her enchanments you can eat her magic herbs"

}
	
treasury={
    
    "name" : "Circe's Treasury",
    "description": "PLACEHOLDER STRING"

}

	

cyclopsEntrance = {

	"name" : "Professer Polys office",      #####??/???/???????//~?????/////??/??/?/??/?
	"description": "Up a short flight of stairs,' Professer Polyphemus's Office ' reads on a semi tranclucent door in bold black gold encompassed letters. """ #this needs fixing with regard to encompassed
        
        ## examine function should print(The top of the doorway seems to be worn, perhaps by some unintentional headbutting. The door looks like you could open it if you so decide')
        ####   "items":"something to awaken the poly...? "
	
"examineDescription":
}

cyclops = {
	
	"name": "Cave of the Cyclops",
        
	"description": "You enter a fluorescently lit office. Aggresive clouds of whiskey vapor arrest your sense of smell water your eyes.
        In the center of the room is a large oak desk with hiking pole leaning on it.

        
        The figure slumped slumbering behind it is a broad shouldered, deepcheasted, stronglimbed, freelyfreckeled, wide mouthed, longheaded, bearkneed, brawnyhanded, ruddyfaced drunkard.
        An eyepatch clings to his skin, inset into his gaping cavernous eyesocket.
        #A powerful rhythmic resonance formidable heart thunderer rumblingly causing the ground, vibrate and tremble and the lofty walls of the office to vibrate and tremble.", 
        The lofty walls of the office pulse rythmically, rumbling in time with the rise and fall of Poly's chest
        
	"items": [umbrella, earbuds, dinghy],
                 #perhaps umberella?
        
	"creatures" : [cyclops]                                              ##### add wake up squince
"examineDescription":
}

sirenCorridor = {
    "name": "The Long Corridor",
        
	"description": "The relentless Cardiffian rain has flooded the corridor. You see two men (one of which is oddly wearing ear muffs) steal your raft although your glad to part with it, they trying to    ",
    #potential for sign language further hints at absence of sound
        
	"items": [],
        
	"creatures" : [],
    
    "examineDescription": 	

}

sirenLair = {

	"examineDescription":

}


""" This handles room definitions . A room is a dictionary with the following attributes 

    Name - string 
    Description - String 
    Items - list of dictionaries 
    Creatures - list of dictionaries
    Examine Description - String

"""
