from entities import *
from items import *

ithaca={
    
  'name':'The leacture hall',

   'description':'place holder string',

    'items':[],

    'creatures':[],

    'examineDescription':'place holder string',
    
    'lowHelp' :  'placeholder string',
    'midHelp' :  'place holder string',
    'highHelp' : 'place holder string',

    'exits':{}

}

calypsoCave={

    

    "name" : """Calypso's cave""",

    "description": """Boggeled minded, you arrive at a place that somewhat resembles your universitys reseption but the only diffrence is that its actaully a cave,
    on an island, in anchent greese""",

    'exits':{

    'east':'cyclopsEntrance',

    'down':'basement',

    'south':'beach',
    
    "north" : "sirenCorridor"},



    'items':[],

    'creatures':[],

    'examineDescription':''' Round about the cave grows luxuriant wood, alder and sweet-smelling cypress, where birds long of wing wont to nest.
    Owls, falcons and sea-crows with chattering tongues ply their business on the sea. ''',


    
    'lowHelp' :  'I hear the beach in horrible this time of year.',
    'midHelp' :  'There are 3 exits from this island',
    'highHelp' : 'Perhaps with the items you find here you will be able to escape!'



}

    

beach={

    

    "name" : """Calypso's island""",

    "description": """You walk down to a bay but far from the Carrabin sandy beaches
creating connotations of mai tais and pineapples, here it rains and thunder seems to have charred the skull and bones flag atop the mast of pirate ship""",



    'examineDescription':"""Time has had toll on the once great ship, it is smashed and battered. The rope hanging from the mast are green and slippery with algae""",
    
    'exits':{'north':'calypsoCave'},

    'items':[rope],

    'creatures':[],
    

    
    'lowHelp' :  'Whatever you do, dont try and go for a swim...',
    'midHelp' :  'What do you need from here?',
    'highHelp' : 'The wreak has some things that could help you escape'


}

    

basement={

    

    "name" : "The Basement",

    "description": """Cobwebs and dust have replaced the white paint here. Against one of the walls a is wooden crate that glares at you threataningly...
    you clench your fists preparing for a show down...""",

    "items": [],

    'exits':{'up':'calypsoCave'},

     
    'creatures':[box],

    'examineDescription':'The crate seems to utter something about your mother under its breath. ',
    
    'lowHelp' :  'Box',
    'midHelp' :  'Perhaps with the items you find here you will be able to escape!',
    'highHelp' : 'Try and think inside the box'

  

}

    

    

circe={

    

    "name" : """Circe's Mansion""",

    "description": """The Mansion you arrive at boasts grand white marble columns and suspiciously colourful flowers placed seemingly at random around the front room. 
    Walking gracefully down the stairs one hand running down the balcony, wearing a long white silk robe and gold framed glasses, is Circe.
    Following her are three abnormally large ginger tabby cats that lay down lazily by the roaring fire. Displayed in the centre of the room, a life size bronze piggy bank with a
    terrified expression.""",

    


    'examineDescription' :"""Round her supple waist is scarlet sash , she has a wildly seductive, crazy, loopy nymphetic air about her.
     Smirking and visably flatterd by your wondering eyes, she reminds you that her eyes, "are up here..."
     
                "It seems you have enraged the great posiden,
            now there is now place for you to hide in,
           give this to the man whose eye you poked out,
           he will no doubt forget what he was angry about,
          and the way to your world will be safe... iden"
          
          you are impressed by her eloquent lymeric and she  passes the Panacea to you.
  
          """,

    'exits':{'up':'treasury',

        'north':'ithaca',},
    
                                                                                               #######how does he get to island again>:?

    'items':[],

    'creatures':[],

    
    'lowHelp' :  'Perhaps command would ferther you in your cause.',
    'midHelp' :  'Could this be anymore obvious?',
    'highHelp' : 'Dont play inocent man  we know whos poked his eye out.'

}

    

treasury={

    "name" : "Circe's Treasury",

    "description": """You walked in to the treasury, candles lite up all all of a sudden! Heads of wolfs and girzzly bears decorate the walls, and the
floor is carpeted with animal fur.`The heads seem to still posses the souls of the animals still watching over the safe.
There is a gold door, the door doesn’t have a lock.""",


    'examineDescription':'A plain safe in the corner requires a 4 digits to unlock',
    

    'exits':{'down':'circe'},


    'items':[],

    'creatures':[],

    
    'lowHelp' :  'There are only 9999 options you have to go throgh really... or perhaps its hidden somewhere and you missed it. ',
    'midHelp' :  'Lets just say the images of the rooms wernt added because of the impressive graphics',
    'highHelp':  'The code is hidden in the rooms, but you must look carfully',


}


cyclopsEntrance = {



    "name" : "Professor Polys office",      

    "description": "Up a short flight of stairs,' Professor Polyphemus's Office' reads on a semi translucent door in bold black letters outlined in gold. """ ,

    "examineDescription":"""The top of the doorway seems to be worn, perhaps by some unintentional headbutting. """,#######how do you know the shout command?>?/???
                                                                                                                        # "items":"something to awaken the poly...? 

    'exits':{'south':'cyclops',

             'west':'calypsoCave'},


    'items':[umbrella],

    'creatures':[],

    'lowHelp' :  'What command could help you now?',
    'midHelp' :  'open sesime would proberly work if you said it load enogh',
    'highHelp' : 'Try and twist and shout, just without the twist'

}



cyclops = {

    "name": "Cave of the Cyclops",

    "description": """You enter a fluorescently lit office. Aggresive clouds of whiskey vapor arrest your sense of smell and cause your eyes to water.
        In the center of the room is a large oak desk with a framed picture of Poly and his father and a black umberella leaning on it.
        The figure slumped behind it is a broad shouldered, deepcheasted, stronglimbed, freelyfreckeled, wide mouthed, longheaded, bearkneed, brawnyhanded, ruddyfaced drunkard.
        An eyepatch clings to his skin, inset into his gaping cavernous eyesocket and A powerful rhythmic resonance of polys formidable heart thunderers rumblingly,
        causing the ground and the lofty walls of the office to vibrate and tremble.""",

        #'me want you is go get me my glass eye is lost hicup'


    "items": [earplug, dinghy],


    "creatures" : [cyclops],###why is this i square braks??                                          


    'exits':{'north':'cyclopsEntrance'},
        


    'examineDescription':'Me want you is go get me my glass eye is lost',
    
    'lowHelp' :  'claptomania migh be bad but hey you need to get to you lecture.',
    'midHelp' :  'did you check your inventory?',
    'highHelp' : 'it not raining but that umberella sure would help',



}



sirenCorridor = {

    "name": "The Long Corridor",

        

    "description": """The relentless Cardiffian rain has flooded the corridor and only the tip tap of the water seeping through the cracks in the roof break the silence.
        You can just about make out the far end where two men are wearing ear protectors. There is an pungent smell of rotting flesh seemingly coming from the depths of the water.""",

    "items": [redHerring],
    "creatures" : [],

    

    "examineDescription":"A red herring swims in circles after its own tail." ,  ### how does this exit work if no earbuds

    'exits':{

        'north':'circe'

        },
    

    
    'lowHelp' :   'You need to cross these waters to get to Ithaca',
    'midHelp' : 'What did you steal from Poly that could help you cross?',
    'highHelp' : 'Proberly wise to follow the two mens example, and that dinghy will take you over the waters'


}



sirenLair = {



     "name": "Cheerleading practice room",

        

    "description": """You wade into the cold water fearlesy with images of Ithica in your mind. You see girls bathing in the water red liped and doe eyed creatures dressed provocatively in blue red and white skirts.
    The little light there reflects of firm pouting breasts and their lustrus song pollutetes your mind with desire as you paddle furiously in their direction.
    The foulest stench is in the air, danger begins to loom, for no mere mortal can resist them, and they close in to seal your doom, """,
                                                                                                        # impregnat thier womb?
    "items": [],

    "creatures" : [siren],

      'exits':{} ,                                                                                ##### if win .... how does this exit work
    'examineDescription':'The hot girls seem to me to be the visible personification of absolute perfection',
    
    'lowHelp' :  'There is no escaping this fight im afraid',
    'midHelp' :  'There is no escaping this fight im afraid',
    'highHelp' : 'There is no escaping this fight im afraid'


}
kryllafight={
    
    'name':'''Encounter with Kirill ''',

   ' description ': ''' The door off the safe flings open and a whirlwind of air compleatly messing up your hairdoo. Soon the swirling wind dies down reveling a bow.''',

    ## take bow should print.... (by taking the bow it seems you have unwittilngly challanged the mighty krilla to a fight, )

    'items':[],

    'creatures':['krylla'],

    'examineDescription':'',
    'exits':{},
    
    
    'lowHelp' :  'Try and Stay alive',
    'midHelp' :  '''If you are feeling this is a fight you can acually win, i recomend trying to read 'The art of war' to make sure you have a chance ''',
    'highHelp' : 'Im sorry kiddo cant help you here im afraid...',

    
         }





rooms = {

     
    'kryllafight':kryllafight,
         
    'calypsoCave':calypsoCave,

    'beach':beach,

    'basement':basement,

    'cyclopsEntrance':cyclopsEntrance,

    'cyclops':cyclops,

    'sirenCorridor':sirenCorridor,

   'sirenLair':sirenLair,

    'treasury':treasury,

    'circe':circe,
    
    'ithaca':ithaca

    
    }
