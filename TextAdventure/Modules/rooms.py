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
    "description": "PLACEHOLDER STRING",

    'exits' :{
    'east':'cyclopsEntrance',
    'down':'basement',
    'south':'beach'}, 
    
    "lowHelp" : "PLACEHOLDER STRING", 
    "midHelp" : "PLACEHOLDER STRING",
    "highHelp" : "PLACEHOLDER STRING"

}
    
beach={
    
    "name" : """Calypso's island""",
    "description": "PLACEHOLDER STRING",
    'exits':{'north':'calypsoCave'}, 
    
    "lowHelp" : "PLACEHOLDER STRING", 
    "midHelp" : "PLACEHOLDER STRING",
    "highHelp" : "PLACEHOLDER STRING"

}
    
basement={
    
    "name" : "The Basement",
    "description": "PLACEHOLDER STRING",
    "creatures": [box],
    'exits':{'up':'calypsoCave'}, 
    
    "lowHelp" : "PLACEHOLDER STRING", 
    "midHelp" : "PLACEHOLDER STRING",
    "highHelp" : "PLACEHOLDER STRING"

}
    
    
Circe={
    
    "name" : """Circe's Mansion""",
    "description": """The Mansion you arrive at boast grand white mabrle collumbs and suspicously coulerfull flowers placed seemingly at random around the front room. 
    Walking down the stairs wearing nothing but a long white silk robe and thinly framedglasses is Circe.
    Following her are three abnormaly large ginger tabby cats that lay down comptemtly by the roaring fire. Displayed in the center of the room life size bronze piggy bank.
    """,
    
    'examineDescription':"""Round her supple waist is scarlet sash , she has a wildly seductive, crazy, loopy nymphetic air about her.
     Smirking and visably flatterd by your wondering eyes, she reminds you that her eyes, "are up here..."   """,



    'exits':{'up':'treasury',
        'north':'ithyca',
        '':''}, 
    
    "lowHelp" : "PLACEHOLDER STRING", 
    "midHelp" : "PLACEHOLDER STRING",
    "highHelp" : "PLACEHOLDER STRING"#######how does he get to island again>:?



}
    
treasury={
    
    "name" : "Circe's Treasury",
    "description": #"""“You walked in to the treasury, candles lit up all all of a sudden!  Wolf heads and girzzlys heads all over the walls and the ground is full of the finest fur carpet a man can ever witness It looked so different to the point where I felt that the fur , heads and everything had the souls of the animals still present in them. There is a gold door, the door doesn’t have a lock.”
#“ there is a safe in the corner”""" # SYNTAX!!!! of both kinds
"placeholder string"
,
    'exits':{'down':'Circe'}, 
    
    "lowHelp" : "PLACEHOLDER STRING", 
    "midHelp" : "PLACEHOLDER STRING",
    "highHelp" : "PLACEHOLDER STRING"

}

    

cyclopsEntrance = {

    "name" : "Professer Polys office",      
    "description": "Up a short flight of stairs,' Professer Polyphemus's Office' reads on a semi tranclucent door in bold black letters outlined in gold. """ ,
        
        "examineDescription":"""The top of the doorway seems to be worn, perhaps by some unintentional headbutting. """,#######how do you know the shout command?>?/???   # "items":"something to awaken the poly...? 
    
    'exits':{'south':'cyclops',
         'east':'''calypsoCave'''}, 
    
    "lowHelp" : "PLACEHOLDER STRING", 
    "midHelp" : "PLACEHOLDER STRING",
    "highHelp" : "PLACEHOLDER STRING"

}

cyclops = {
    
    "name": "Cave of the Cyclops",

    "description": """You enter a fluorescently lit office. Aggresive clouds of whiskey vapor arrest your sense of smell cause your eyes to water.
        In the center of the room is a large oak desk with a black umberella leaning on it.
    The figure slumped behind it is a broad shouldered, deepcheasted, stronglimbed, freelyfreckeled, wide mouthed, longheaded, bearkneed, brawnyhanded, ruddyfaced drunkard.
        An eyepatch clings to his skin, inset into his gaping cavernous eyesocket and A powerful rhythmic resonance of polys formidable heart thunderers rumblingly,
        causing the ground and the lofty walls of the office to vibrate and tremble.""",
        
        
    "items": [umbrella, earplug, dinghy],
    #item umberrela should be pointy and have something tieing in with theme carved on the edge of it
                 
        
    "creatures" : [cyclops],  ###why is this i square braks??                                          
"examineDescription":"PLACEHOLDER STRING",


        'exits':{'north':'cyclopsEntrance'}, 
    
    "lowHelp" : "PLACEHOLDER STRING", 
    "midHelp" : "PLACEHOLDER STRING",
    "highHelp" : "PLACEHOLDER STRING"

}

sirenCorridor = {
    "name": "The Long Corridor",
        
    "description": """The relentless Cardiffian rain has flooded the corridor and only the tif taf of the water seeping throgh the cracks in the roof break the silence.
    You can just about make out the far end where two men are wearing ear protectors.  There is an pungent smell of rotting flesh 
    """,
        
    "items": [redHerring],
        
    "creatures" : [],
    
    "examineDescription":"A red herring swims in circles after its own tail.",### how does this exit work if no earbuds
    'exits':{
        '?/????':'sirens lair',
        'north':'Circe'
        }, 
    
    "lowHelp" : "PLACEHOLDER STRING", 
    "midHelp" : "PLACEHOLDER STRING",
    "highHelp" : "PLACEHOLDER STRING"

}

sirenLair = {

     "name": "Cheerleading practice room",
        
    "description": """you wade into the cold water fearlesy with images of Ithica in your mind. You see girls bathing in the water red liped and doe eyed creatures dressed provocatively in blue red and white skirts.
    The little light there reflects of firm pouting breasts and their lustrus song pollutetes your mind with desire as you paddle furiously in their direction.   """,
        
    "items": [],
        
    "creatures" : [siren],
    
    'exits':{'':''}, 
    
    "lowHelp" : "PLACEHOLDER STRING", 
    "midHelp" : "PLACEHOLDER STRING",
    "highHelp" : "PLACEHOLDER STRING"   ##### if win .... how does this exit work
     
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

def printRoom(currentRoom):
    
    print("\n" + currentRoom["name"].upper() + "\n" + currentRoom["description"])