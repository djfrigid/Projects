#Type "copyright", "credits" or "license()" for more information.

#>>> from items import *

from entities import *
from items import *

print('''       Out into the rain in miserable Cardiff you go, after reading an article about the amount of 
	deaths caused by pharmacy errors(1 in 1000!).
	You are hunched over with a cigarette in your mouth, it goes out seconds after it was lit after 
	a BMWx5 sped through a puddle.
	Treating yourself to Tescos' 3 pound meal deal, you arrive at the pharmacy. The slippers you 
	are wearing are visibly soaked, they squelch as you approach the counter. The woman
	behind it looks at you judgingly, visibly unimpressed, and when you ask for a box of flu medicine,
	she returns squinting at the box in her hand, seemingly unable to read it without
	her glasses. She hands you a box of 'Oddssydinazacitidine'.
       
       'POSSIBLE SIDE AFFECTS MAY INCLUDE':
        *Causing serious tranformation of reality, passing body and mind to hyperquantum capacities,
        *Magicular particles in your vicinity may double to relative inevitability,
        *Fractal dimensions above infinity+1 collapsing into a finite equilibrium.
        *Mild nausea
        *Drowsiness
        
        You take it politely without question, reasoning that 1 in 1000 is a tremendously small percentage...
        As you start the 10 minute walk back to your lectures, you pop 3 of the little yellow pills.
        Suddenly you heart starts to thump, your knees become weak...
          

    ''')


""" This handles room definitions . A room is a dictionary with the following attributes 



'name':'namemcnameface'

'description':'place holder string',

'items':[],

'creatures':[],

'examine Description':'place holder string',
    
'lowHelp' :  'place holder string',
'midHelp' :  'place holder string',
'highHelp' : 'place holder string',

'exits'{}

"""





ithaca={
    'name':'The Lecture Hall',

    'description ':"""Thank the Gods you are finally home! But wait, your home is infested with hundreds of men all
    hoping for your wife's hand in marriage. Your wife looks as young as the day you left, but the years have not
    been as kind to you, she is doubtful of your claim to be her Ulysses. She asks you to recount details of your
    journey, the Gods will tell her if you are being truthful.

    'If you are my darling Ulysses, then you will answer me this:'

    'What do Cerce's sash, a lonely fish, and the skirts of the Sirens have in common?'

    """,

    'items':[],

    'creatures':[],

    'examine Description':'place holder string',
    
    'lowHelp' :  'placeholder string',
    'midHelp' :  'place holder string',
    'highHelp' : 'place holder string',

    'exits':{}
}

calypsoCave={
    "name" : """Calypso's cave""",

    "description": """  Your mind boggled, you arrive at a place that somewhat resembles your university's 
    reception, the only difference is that it's actually a cave, on an island, in Ancient Greece
    _____________________________________________
    |  | '' '  /        |'' ' |      \'  ' '|     |
    |   \' '  /         |' '' /       | ' ''/     |
    |    \ ''|  	\ '' /	      \' ' |      |	      
    |     |  /           \ '|          \' /       | 
    |      \/             | /           \/       |
    |                     \/                     |
    |                                            |
    |                           # #### ####      |
    |                         ### \/#|### |/#### |
    |                        ##\/#/ \||/0#/_/##/_|
    |                       ###  \/###|/4\/ # ###|
    |                    ##_\_#\_\## | #5###_/_##|
    |       \. _(9>     ## #### # \ #| /1 #### ##|
    |        \==_)       __#_--###`  |{,###---###|
    |  _______-'=___________       \ }{          |
    |  |    [Reception]    |        }}{          |
    |  |                   |        }}{          |
    |  |___________________|        {{}          |        
    |                         , -=-~{ .-^- _     |""",

    'items':[],

    'creatures':[],

    'examineDescription':'''Around about the cave there grows luxuriant wood, alder and sweet-smelling 
    cypress, where birds long of wing go to nest.
    Owls, falcons and sea-crows with chattering tongues ply their business on the sea. ''',
    
    'lowHelp' :  'I hear the beach is horrible this time of year.',
    'midHelp' :  'There are 3 exits from this island',
    'highHelp' : 'Perhaps with the items you find here you will be able to escape!',

    'exits':{'east':'cyclopsEntrance','down':'basement',"north" : "sirenCorridor",'south':'beach'}
}

beach={
    "name" : """Calypso's island""",

    "description": """  You walk down to a bay but far from the Caribbean sandy beaches creating images of
    mai tais and pineapples, here it rains and thunder seems to have charred the skull and bones flag 
    atop the mast of pirate ship
    _____________________________________________
    |                                            |
    |           4                                |
    |                      1                     |          				     
    |                5                           |
    |  0                                         |       
    |                         _\/_               |
    |          _              //o\  _\/_         |
    |__ __ ___(_)_ __ __ ____ _ | __/o\\ _        |
    |_=_-=-=-_-__=_-= _=_=-=_,-'|"'""-|-,_       |
    |--_- =- _=-=- -_=-=_,-"  /|      |          |
    |-_ -=- =- =- -=.--"     / |      __     .   |
    |_=-=-_-_=-=_,-"        /__|__               |
    |-=_-_=-=_,-"         \--------/       .     |
    | -_=_,-"                                    |
    |=_-"		__                  __   |
    |-"    .                  .                  |
    |            .                    .     .    |
    |                        __          __      |
    |   __                                       |""",

    'items':[rope],

    'creatures':[],

    'examineDescription':"""Time has taken its toll on the once great ship, it is smashed and battered. 
    The ropes hanging from the mast are green and slippery with algae""",

    'lowHelp' :  'Whatever you do, dont try and go for a swim...',
    'midHelp' :  'What do you need from here?',
    'highHelp' : 'The wreck has some things that could help you escape',

    'exits':{'north':'calypsoCave'}
}

basement={
    "name" : "The Basement",

    "description": """  Cobwebs and dust have replaced the white paint here. Against one of the walls is 
    a wooden crate that glares at you threateningly...
    You clench your fists preparing for a showdown...
    _____________________________________________
    | ## #  |                         ## #       |
    |  ## # | [0451]      __.--'-.   ####        |
    |##  #  |       __.--'        `-. ##         |		     
    |       | __.--'                 `-          |
    |       ||.                  __.--||         |
    |       |||`-.         __.--'     ||         |
    |       |||   `- __.--'           ||         |   
    |       |||    |||                ||         |
    |       |||    |||                ||_________|
    |       |||    |||                ||         |
    |       /||    |||                ||         |
    |      / ||    |||                ||         |
    |     /  ||    |||                ||         |
    |    /   ||    |||           __.--'          |
    |   /      `-. |||     __.--'                |
    |  /          `-||_.--'                      |
    | /                                          |
    |/                                           |
    |                                            |""",

    "items": [],
     
    'creatures':[box],

    'examine Description':'The crate seems to utter something about your mother under its breath. ',
    
    'lowHelp' :  'Box',
    'midHelp' :  'Perhaps with the items you find here you will be able to escape!',
    'highHelp' : 'Try and think inside the box',

    'exits':{'up':'calypsoCave'}
}

circe={
    "name" : """Circe's Mansion""",

    "description": """  The Mansion you arrive at boasts grand white marble columns and suspiciously 
    colourful flowers placed seemingly at random around the front room. 

    Walking gracefully down the stairs one hand running down the balcony, wearing a long white silk 
    robe and gold framed glasses, is Circe.

    Following her are three abnormally large ginger tabby cats that lay down lazily by the roaring fire.
    Displayed in the centre of the room, a life size bronze piggy bank with a
    terrified expression.
    _____________________________________________
    |                           (_,.....,_)      |
    |                             |||||||        | 
    |             w*W*W*W*w       |||||||        | 
    |              \"."."/        |||||||        |
    |               //`\\         |||||||        |
    |              (/- -\)        |||||||        |
    |              (\_-_/)        |||||||        |
    |             .-~'='~-.       |||||||        |
    |            /`~`"Y"`~`\      |||||||        |
    |           / /(_ * _)\ \     |||||||        |
    |          / /  )   (  \ \    |||||||        |
    |          \ \_/\\_//\_/ /    |||||||        |
    |           \/_) '*' (_\/     |||||||        |
    |             |       |       |||||||        |
    |          _;_|       |      ,_______,       |
    |        ,'o  |       |        )   (         |
    |       [_,   |       |      ,      `        |
    |        `._  |       |    _/_________\_     |
    |           ll|       |   |_____________|    |""",

    'items':[],

    'creatures':[],

    'examineDescription' :"""Round her supple waist is deep red sash , she has a wildly seductive, crazy, 
    loopy nymphetic air about her.

     Smirking and visibly flatterd by your wondering eyes, she reminds you that her eyes, "are up here..."
     
                "It seems you have enraged the great posiden,
            now there is no place for you to hide in,
           give this to the man whose eye you poked out,
           he will no doubt forget what he was angry about,
          and the way to your world will be safe... iden"
          
          you are impressed by her eloquent rhyme and she passes the Panacea to you.
  
          """,
    
    'lowHelp' :  'Perhaps a command would further your cause.',
    'midHelp' :  'Could this be anymore obvious?',
    'highHelp' : 'Dont play innocent man, we know who poked his eye out.',

    'exits':{'up':'treasury','north':'ithaca','south':'sirenCorridor'},

}

treasury={

    "name" : "Circe's Treasury",

    "description": """  The candles ignite as you walk into the treasury, the heads of wolves and great bears 
    decorate the walls, and the floor is carpeted with animal fur.`The heads seem to still posses the souls 
    of the animals, watching over the safe.
    There is a gold door, the door doesn’t have a lock.
    _____________________________________________
    |                                            |
    |                                            |
    |                                            |
    |                                 (\         |
    |	                          .'.        |
    |           +--------------+      | |        |
    |          /              /|      | |        |
    |         /              / |      |_|        |
    |        *--------------*  |      ) (        |
    |        |              |  |       |         |
    |        |   [ENTER]    |  |      / \        |
    |        |              |  |    _}___{_      |
    |________|     (o)      |  +____|     |______|
    |        |   [----]     | /     |     |      |
    |        |              |/      |     |      |
    |        *--------------*       |     |      |
    |                               |     |      |
    |                               |     |      |
    |                               |     |      |""",

    'items':[],

    'creatures':[],

    'examineDescription':'A plain safe in the corner requires a 4 digit code to unlock',

    'lowHelp' :  'There are only 10,000 options you have to go through really... or perhaps its hidden somewhere and you missed it. ',
    'midHelp' :  """Lets just say the images of the rooms weren't added because of the impressive graphics""",
    'highHelp':  'The code is hidden in the rooms, but you must look carefully',

    'exits':{'down':'circe'}
}


cyclopsEntrance = {
    "name" : "Professor Polys office",      

    "description": """  At the entrance of a cave,' Professor Polyphemus's Office' reads on a hardwood door in 
    bold black letters outlined in gold.
    _____________________________________________
    |                                            |
    |                                            |
    |  # #  ##                   ### \/#|### |/##|                                            
    | ## ##  # ##               ##\/#/ \||/##/_/#|                           
    |## 0\/#\|# ()|           ###  \/###|/ \/ # #|
    |#\/4/#/#||/# /_        ##_\_#\_\## | #/###_/|
    | #\5#|()|/#\/ '       ## #### # \ #| /  ####|
    | #_1 |# |##/___..-.    __#_--###`  |{,###---|
    |  # #| #|._/  __ \_`-.__         \ }{       |
    |    #\#\|#/ .'/__ \_ `-. \--.     }}{       |
    |      \||.-_/#|  |#\  /-' `\_      }}{      |
    |       |||/###| .|##\_  \._   `-   {{}      |
    | ""'   |_|####|  |####\_`.  -' \=-~{ .-^- _ |
    |""'"'	 " "'"''"'   '" ''"'"''"   `}"''"|  
    | ""'""        ""'"''    "'""      ""'""     |
    |""     "'"" ''""          '"'""'            |
    | "''"" "'"'       "'''" "'         ""' ""'  |
    |    ""'"'"     ""''""'       ""''""'      "'|
    |                                            |""",

    'items':[umbrella],

    'creatures':[],

    "examineDescription":"""The top of the doorway seems to be worn, perhaps by some unintentional headbutting.""",

    'lowHelp' :  'What command could help you now?',
    'midHelp' :  'Open sesame would probably work if you said it loud enough',
    'highHelp' : 'Try and twist and shout, just without the twist',

    'exits':{'south':'cyclops','west':'calypsoCave'}
}

cyclops = {
    "name": "Cave of the Cyclops",

    "description": """  You enter a fluorescently lit office. Aggresive clouds of whiskey vapor attack your 
    sense of smell and cause your eyes to water.

    In the center of the room is a large oak desk with a framed picture of Poly and his father and a black
    umberella leaning on it.

    The figure slumped behind it is a broad shouldered, deepchested, stronglimbed, freelyfreckeled, wide mouthed,
    longheaded, bearkneed, brawnyhanded, ruddyfaced drunkard.

    An eyepatch clings to his skin, inset into his gaping cavernous eyesocket and a powerful rhythmic resonance 
    of polys formidable heart thunderers rumblingly,

    causing the ground and the lofty walls of the office to vibrate and tremble.
    _____________________________________________
    |                  ,#####,                   |
    |                  #_____#                   |
    |                  |(_O_)|                   |
    |                  |  u  |                   |
    |                  \  =  /                   |
    |                  |\___/|                   |
    |         ___ ____/:     :\____ ___          |
    |       .'   `.-===-\   /-===-.`   '.        |
    |      /      .-"" ""-.-"" ""-.      \       |
    |     /'             =:=             '\      |
    |     | ' .:    o   -=:=-   o    :    |      |
    |     |     |. '-.....-'-.....-'|    '|      |
    |     | '    \.     --:--     . / :   |      |
    |     \ '  :  \__________--____/      /      |
    |      \     :        '    |    '    /       |
    |  _____\__________________|________/______  |
    | ||        [Professer Polypheus]         || |
    | ||======================================|| |                     
    | ||                                      || |""",

    "items": [earplug, dinghy],

    "creatures" : [cyclops],                                         

    'examine Description':'Me want you is go get me my glass eye is lost',

    'lowHelp' :  'Claptomania migh be bad but hey you need to get to you lecture.',
    'midHelp' :  'Did you check your inventory?',
    'highHelp' : 'It not raining but that umberella sure would help',

    'exits':{'north':'cyclopsEntrance'}
}

sirenCorridor = {

    "name": "The Long Corridor",

    "description": """  The relentless Cardiffian rain has flooded the corridor and only the tip tap of the 
    water seeping through the cracks in the roof breaks the silence.
    You can just about make out the far end where two men are wearing ear protectors. There is an pungent 
    smell of rotting flesh seemingly coming from the depths of the water.
    ______________________________________________
    |.'',                                     ,''.|
    |.'.'',                                 ,''.'.|
    |.'.'.'',                             ,''.'.'.|
    |.'.'.'.'',                         ,''.'.'.'.|
    |.'.'.'.'.|                         |.'.'.'.'.|
    |.'.'.'.'.|===;                 ;===|.'.'.'.'.|
    |.'.'.'.'.|:::|',             ,'|:::|.'.'.'.'.|
    |.'.'.'.'.|---|'.|, _______ ,|.'|---|.'.'.'.'.|
    |.'.'.'.'.|:::|'.|'|0451045|'|.'|:::|.'.'.'.'.|
    |,',',',',|---|',|'|1045104|'|,'|---|,',',',',|
    |.'.'.'.'.|:::|'.|'|5104510|'|.'|:::|.'.'.'.'.|
    |.'.'.'.'.|---|',/~~~~~ ~~~~~\,'|---|.'.'.'.'.|
    |.'.'.'.'.|~~~~~~~~~  ~~~~~~~~~~~~~~|.'.'.'.'.|
    |.'.'.'._/~~~~~~~~~~~~     ~~~~~~.~~~\_.'.'.'.|
    |.'.'.'/~~~~~~~    ~~~~~~~~~~~~~~~~~~~~\'.'.'.|
    |.'.'./~~~~~~~~~~~~~~~~~~~~~    ~~~~~~~~\.'.'.|
    |.'.'|~~~~~~~~~.~~~~~~~~~~  ~~~~~~~~~~~~|,'.'.|
    |.'_/~~~~~~~~~~~~~~~~~    ~~~~~~~~~~~~~~~\_,'.|
    |;/~~~~~~~.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\',|""",

    "items": [redHerring],
    
    "creatures" : [],

    "examineDescription":"A red herring swims in circles after its own tail.",
    
    'lowHelp' :   'You need to cross these waters to get to Ithyca',
    'midHelp' : 'What did you steal from Poly that could help you cross?',
    'highHelp' : 'Probably wise to follow the two mens example, and that dinghy will take you over the waters'

    'exits':{'north':'circe'},
}

sirenLair = {
    "name": "Cheerleading practice room",

    "description": """  You wade into the cold water fearlesy with images of Ithyca in your mind.
    'These girls seem to be the visible personification of absolute perfection'

    The little light there reflects of firm pouting breasts and their lustrus song pollutes your mind with 
    desire as you paddle furiously in their direction.
    The foulest stench is in the air, danger begins to loom, for no mere mortal can resist them, and they 
    close in to seal your doom.
    _____________________________________________
    |                                            |
    |                                            |
    |       .--.                                 |
    |      /`._ `.                               |
    |     | /. .` \                              |
    |     / ) _ ( /                 _.._         |
    |    | /.`-' \-.              .'    '.       |
    |    / )`.   (  \            (____/`\ \      |
    |    | .  \^  \_|           (  |' ' )  )     |
    |    |_|`. \`-| |           )  _\- _/  (     |
    |    //   ' \`\ | __..---.(`_.'  ``\    )    |
    |   .'--._.\ .| |`;-""-._(_         `; (     |     
    |__/   `/-._`.`-./      |`-`'--'     ; )_____|
    |  |   /     `-._ `._/  |         ,|_|(      |
    |   `./_.----`  `.' /-,.|___.-'--'_| |_)     |
    | _.--`      _.-' ,'__|   / .........'       |
    |'.__..--````;--"`;   |   `-`                |                
    |             `'..__.'                       |          
    |                                            |""",

    "items": [],

    "creatures" : [siren],

    'examineDescription':"""The girls are bathing in the water, dressed provocatively in bright red skirts.""",

    'lowHelp' :  'There is no escaping this fight im afraid',
    'midHelp' :  'There is no escaping this fight im afraid',
    'highHelp' : 'There is no escaping this fight im afraid',

    'exits':{}, 
}

kryllafight={
    'name':'''Encounter with Kirill ''',

    'description ': ''' The door of the safe flings open and a whirlwind of air completely messing up your 
   hairdo. Soon the swirling wind dies down revealing a bow.''',

    'items':[],

    'creatures':['krylla'],

    'examine Description':'',
    
    'lowHelp' :  'Try and Stay alive',
    'midHelp' :  '''If you are feeling this is a fight you can acually win, i recommend trying to read 'The Art of War' to make sure you have a chance ''',
    'highHelp' : "Im sorry kiddo cant help you in here I'm afraid...",
    'exits':{},
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

