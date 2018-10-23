

#Type "copyright", "credits" or "license()" for more information.



#>>> from items import *






print('''Out into the rain in misrable cardiff you go after reading an artical the amount of deaths caused by pharmasys errors(1 in 1000!).
        Hunched over and cigarette in mouth it goes out as soon as light it after a BMWx5 throgh a puddle.
       Treating yourself to tescos 3 pound meal deal, you arrive at the pharmacy. The slippers you are wearing are visibly soaked squelch as you approch the counter. The woman
       behind it looks at you judgingly visably unimpressed and when you ask for a box of flu medicine, she goes and returns squinting at the box in  her hand, obiously unable to read without
       her glasses, and hands you a box of 'Oddssydinazacitidine'.
       
       'POSSIBLE SIDE AFFECTS MAY INCLUDE':
        *Causing searious tranformation of our reality passing body and mind to hyperquantum capasitys',
        *Magicular particals in your vesinaty may double to relitive inevitability,
        *Fractal dimentions above infinity+1  collapsing into an finiate equilibriam.
        *Mild nausea
        *Drowsynes
        
        You take it politely with out question, reasoning that with any luck you could be the 1 in 1000...
        As you start you 10 minuit walk to your lectures, you pop 3 of the little yellow pills.
        Heart starts to thump, knees become weak...
          

    ''')



  #  name - string 

  #  description - String 
#
  #  items - list of dictionaries 

#    creatures - list of dictionaries

  #  examine Description - String
    
    #lowHelp - String - the Low WIS hint
    
  #  midHelp - String - the mid WIS hint
    
  #  highHelp - String - the high WIS hint

#    exits - dictionary











""" This handles room definitions . A room is a dictionary with the following attributes 



    'name':'namemcnameface'

   ' description ':'place holder string',

    'items':[],

    'creatures':[],

    'examine Description':'place holder string',
    
    'lowHelp' :  'place holder string',
    'midHelp' :  'place holder string',
    'highHelp' : 'place holder string',

    'exits'{}

"""





ithaca={
  'name':'namemcnameface',

   ' description ':'place holder string',

    'items':[],

    'creatures':[],

    'examine Description':'place holder string',
    
    'lowHelp' :  'place holder string',
    'midHelp' :  'place holder string',
    'highHelp' : 'place holder string',

    'exits':{}

}

calypsoCave={

    

    "name" : """Calypso's cave""",

    "description": """Boggeled minded, you arrive at a place that somewhat resembles your universitys reseption but the only diffrence is that its actaully a cave,
    on an island, in anchent greese""",

    'exits':{

	'east':'Cyclops entry',

	'down':'Basement',

	'south':'Beach'},



    'items':[],

    'creatures':[],

    'examine Description':'place holder string',
    
    'lowHelp' :  'place holder string',
    'midHelp' :  'place holder string',
    'highHelp' : 'place holder string'



}

	

beach={

    

    "name" : """Calypso's island""",

    "description": """You walk down to a bay but far from the Carrabin sandy beaches
creating connotations of mai tais and pineapples, here it rains and thunder seems to have charred the skull and bones flag atop the mast of pirate ship""",



    'examineDescription':"""Time has had toll on the once great ship, it is smashed and battered. The ropes hanging from the mast are green and slippery with algae""",
    
    'exits':{'north':'calypsoCave'},

    'items':['rope'],

    'creatures':[],

    
    'lowHelp' :  'place holder string',
    'midHelp' :  'place holder string',
    'highHelp' : 'place holder string'


}

	

Basement={

    

    "name" : "The Basement",

    "description": """Cobwebs and dust have replaced the white paint here. Against one of the walls a is wooden crate that glares at you threataningly...
    you clench your fists preparing for a show down...""",

    "items": [],

    'exits':{'up':'calypsoCave'},

     
    'creatures':[box],

    'examine Description':'place holder string',
    
    'lowHelp' :  'place holder string',
    'midHelp' :  'place holder string',
    'highHelp' : 'place holder string'

  

}

	

    

circe={

    

    "name" : """Circe's Mansion""",

    "description": """The Mansion you arrive at boast grand white marble columns and suspiciously colourful flowers placed seemingly at random around the front room. 

    Walking gracefully down the stairs one hand running down the balcony, wearing a long white silk robe and gold framed glasses, is Circe.

    Following her are three abnormally large ginger tabby cats that lay down lazily by the roaring fire. Displayed in the centre of the room, a life size bronze piggy bank with a
    terrified expression.""",

    
           #'''it seems you have enraged the great posiden,
          #  now there is now place for you to hide in,
         #  give this to the man whose eye you poked out,
          # he will no doubt forget what he was angry about,
         #  and the way to your world will be safe.... iden
        
           # '''
       
    #Panacea

    

    'examineDescription' :"""Round her supple waist is scarlet sash , she has a wildly seductive, crazy, loopy nymphetic air about her.

     Smirking and visably flatterd by your wondering eyes, she reminds you that her eyes, "are up here..."   """,



    'exits':{'up':'treasury',

	    'north':'ithyca',

	},
    #######how does he get to island again>:?




    'items':[],

    'creatures':[],

    'examine Description':'place holder string',
    
    'lowHelp' :  'place holder string',
    'midHelp' :  'place holder string',
    'highHelp' : 'place holder string'

}

	

treasury={

    "name" : "Circe's Treasury",

    "description": """You walked in to the treasury, candles lite up all all of a sudden! Heads of wolfs and girzzly bears decorate the walls, and the
floor is carpeted with animal fur.`The heads seem to still posses the souls of the animals still watching over the safe.
There is a gold door, the door doesn’t have a lock.""",


    'examineDescription':'A plain safe in the corner requires a 4 digits to unlock',
    

    'exits':{'down':'Circe'},


    'items':[],

    'creatures':[],

    
    'lowHelp' :  'place holder string',
    'midHelp' :  'place holder string',
    'highHelp' : 'place holder string',


}


cyclopsEntrance = {



	"name" : "Professor Polys office",      

	"description": "Up a short flight of stairs,' Professor Polyphemus's Office' reads on a semi translucent door in bold black letters outlined in gold. """ ,

        "examineDescription":"""The top of the doorway seems to be worn, perhaps by some unintentional headbutting. """,#######how do you know the shout command?>?/???
                                                                                                                        # "items":"something to awaken the poly...? 

        'exits':{'south':'cyclops',

	         'west':'calypsoCave'},


    'items':[],

    'creatures':[],

    'lowHelp' :  'place holder string',
    'midHelp' :  'place holder string',
    'highHelp' : 'place holder string'

}



cyclops = {

	"name": "Cave of the Cyclops",

	"description": """You enter a fluorescently lit office. Aggresive clouds of whiskey vapor arrest your sense of smell and cause your eyes to water.

        In the center of the room is a large oak desk with a framed picture of Poly and his father and a black umberella leaning on it.

	The figure slumped behind it is a broad shouldered, deepcheasted, stronglimbed, freelyfreckeled, wide mouthed, longheaded, bearkneed, brawnyhanded, ruddyfaced drunkard.

        An eyepatch clings to his skin, inset into his gaping cavernous eyesocket and A powerful rhythmic resonance of polys formidable heart thunderers rumblingly,

        causing the ground and the lofty walls of the office to vibrate and tremble.""",

        #'me want you is go get me my glass eye is lost hicup'


	"items": [umberella, earbuds, dinghy],


	"creatures" : [cyclops],###why is this i square braks??                                          


        'exits':{'north':'cyclopsEntrance'},
        


    'examine Description':'place holder string',
    
    'lowHelp' :  'place holder string',
    'midHelp' :  'place holder string',
    'highHelp' : 'place holder string',



}



sirenCorridor = {

    "name": "The Long Corridor",

        

	"description": """The relentless Cardiffian rain has flooded the corridor and only the tip tap of the water seeping through the cracks in the roof break the silence.

                        You can just about make out the far end where two men are wearing ear protectors.
                        There is an pungent smell of rotting flesh seemingly coming from the depths of the water.

                            """,

	"items": [redherring],

        

	"creatures" : [],

    

    "examineDescription":"A red herring swims in circles after its own tail." ,  ### how does this exit work if no earbuds

    'exits':{

	    'north':'Circe'

	    },
    

    
    'lowHelp' :  'place holder string',
    'midHelp' :  'place holder string',
    'highHelp' : 'place holder string'


}



sirenLair = {



	 "name": "Cheerleading practice room",

        

	"description": """You wade into the cold water fearlesy with images of Ithica in your mind. You see girls bathing in the water red liped and doe eyed creatures dressed provocatively in blue red and white skirts.

	The little light there reflects of firm pouting breasts and their lustrus song pollutetes your mind with desire as you paddle furiously in their direction.
	The foulest stench is in the air, and they close in to seal your doom, no mere mortal can resist,  """,
                                                                                                        # impregnating thier womb?
	"items": [],

	"creatures" : [sirens],

      'exits':{} ,  ##### if win .... how does this exit work


         

    'examine Description':'place holder string',
    
    'lowHelp' :  'place holder string',
    'midHelp' :  'place holder string',
    'highHelp' : 'place holder string'


}
kryllafight={
    'name':'''Encounter with Kirill '''

   ' description ': ''' The door off the safe flings open and a whirlwind of air compleatly messing up your hairdoo. Soon the swirling wind dies down reveling a bow.''',

    ## take bow should print.... ()

    'items':[],

    'creatures':['krylla'],

    'examine Description':'place holder string',
    
    'lowHelp' :  'place holder string',
    'midHelp' :  'place holder string',
    'highHelp' : 'place holder string',

    'exits'{}
    
    
         }





rooms = [

	 
    kryllafight+,
         
    calypsoCave,

    beach,

    basment,

    cyclopsEntrance,

    cyclops,

    sirenCorridor,

    sirenLair,

    treasury,

    circe,
    
    ithaca

    
    ]

  


#Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
#SyntaxError: invalid syntax
#>>> 
