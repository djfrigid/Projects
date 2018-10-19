import re, random
import player from entities

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

    noPunct = remove_punct(userInput).lower()

    iwords = [] 

    iwords = re.sub(r"[^\w]", " ",  userInput).split()
    
    iwords = filter_words(iwords, skip_words)
    
    return iwords

def divineIntervention(): #this as present can be abused , consider adding a penalty
    prayer = random.randint(0,100)

    if prayer in range(0,51):
      print("You fall to your knees in prayer, petitioning the gods for aid... They ignore you.")
    elif prayer in range(51,56):
      print("You fall to your knees in prayer, petitioning the gods for aid... you are answered ")
    elif prayer in range(56,61):
      print("δεν μπορείτε να διαβάσετε αυτό το ... εκτός αν υποθέτω ο Έλληνας σας. Ωστόσο, αν μπορείτε, κρατήστε αυτό για τον εαυτό σας.")
    elif prayer in range(61,66):
      print("") #joke -mu
    elif prayer in range(66,71):
      print("") #joke -mu
    elif prayer in range(71,76):
      print("You fall to your knees in prayer, petitioning the gods for aid... Your pocket grows strangely heavy and starts wriggling, emitting a slew of eey-ooh's. ") #joke -joke item
    elif prayer in range(76,81):
      print("")#joke - visual appealing
    elif prayer in range(81,86):
        
        d2 = random.randint(0,2)
        if d2 == 0:
            print()# insert flavourtext here
            player["CON"] += 2
        else:
            player["CON"] -= 1
            
    elif prayer in range(86,91):
      print("") #
    elif prayer in range(91,96):
      print("You fall to your knees in prayer, petitioning the gods for aid... Your prayer is answered, your mind filling with forbidden knowledge.") #useful - restores some hints
    elif prayer in range(96,101):
      print("You fall to your knees in prayer, petitioning the gods for aid... and your prayers are answered. You feel a warm energy suffuse through your body before it turns blindingly hot and you are burned to a cinder by divine power ")
      exit()
      #death


#
