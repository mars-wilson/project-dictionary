
# Hello!  This is our first big project!

import json


def loadDict(dictPath = 'dictionary.json'):
    """Return a dict of a specified dictionary json file, defaults to dictionary.json
    
    Args:
        dictPath (str): Optional path to dictionary

    Raises:
        FileNotFoundError: Dict file not there
        JSONDecodeError:  File problem with the dict file
    
    Returns:
        Dictionary as a dict
    """
    dictfile = open(dictPath)
    return json.load(dictfile)

def getCleanWord(word, wordlist):
    """Find the word in the wordlist and return it, otherwise return none
    """
    word = word.strip()
    if word in wordlist:
        return word
    if word.capitalize() in wordlist:
        return word.capitalize()
    if word.lower() in wordlist:
        return word.lower()
    if word.upper() in wordlist:
        return word.upper()
    return None

def printDefinitions(d, word):
    """ prints the definitions of a word, or prints a message if not present. 
    No side effects - does not change the dictionary.
    Does not return anything.
    """
    goodword = getCleanWord(word, d.keys())
    if not goodword:
        print(f"{word} is not in the dictonary."   ) 
    else:
        word = goodword # We don't need the goodword variable anymore - we've found the word we want.
        #print(f"{word}  is in there!  Looks like {goodword}")
        definitions = d[word]
        print( ('Definition' if len(definitions) == 1 else 'Definitions'), 'of', word, ': ')
        for i in range(len(definitions)):
            print(f"Definition {i+1}:")
            print(d[word][i])
            print()


#
#  Here we implement the main menu.
#

d = loadDict()
done = False
while not done:
    print("What do you want to do. Create a new word and def, Read (lookup), Update (add or change a def), or Delete a def?  ")
    action = input("Leave blank or type Quit to quit: ")
    if not action:
        done = True
    else:
        # Note - action is guaranteed to have len > 0 because we're in the else.
        actionFirst = action[0].upper()
        if actionFirst == 'C':
            print("Not ready for that yet.")
        elif actionFirst == 'R':
            word = input("What's the word you want to look up? ")
            if word:
                printDefinitions(d, word)
        elif actionFirst == 'U':
            print("Not ready for that yet.")
        elif actionFirst == 'D':
            print("Not ready for that yet.")
        elif actionFirst == 'Q':
            done = True
        else:
            print("Huh? Dude.  Can you READ?")
        


            




