import re, random

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

def divineIntervention():
    prayer = random.randint(0,100)

    if prayer in range(0,50):
      print("You fall to your knees in prayer, petitioning the gods for aid. They ignore you.")
    elif prayer in range(51,56):
      print("")

