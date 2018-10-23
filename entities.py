"""This file is where the player and any enemies should be defined as dictionaries , they need the following information:

        a name 
        STR - how much damage they should be capable of doing to the player
        DEX - how hard the creature should be to hit
        CON - how much health the creature has 
        
"""

player = {
    
    "name" : "Ulysses", 
    "STR" : 5,
    "DEX" : 5, 
    "CON" : 5,
    "WIS" : 5,
    "STA" : 5, 
    "inventory" : [],
    "MAXCON": 10
        
}

siren = {
    
    "name" : "Siren",
    "STR" : 2,
    "DEX" : 3,
    "CON" : 10
    
}

box = {
    
    "name": "Box", 
    "STR" : 0,
    "DEX" : 0,
    "CON" : 10
    
    }

cyclops = {
    
    "name":"Polyphemus", 
    "STR":7,
    "DEX":1,
    "CON":30    
}
