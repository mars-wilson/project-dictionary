
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
        word = goodword
        #print(f"{word}  is in there!  Looks like {goodword}")
        definitions = d[word]
        print( ('Definition' if len(definitions) == 1 else 'Definitions'), 'of', word, ': ')
        for i in range(len(definitions)):
            print(f"Definition {i+1}:")
            print(d[word][i])
            print()


def updateDefinitionOfWord(d, word):
    """ prints the definitions of a word, or prints a message if not present. 
    No side effects - does not change the dictionary.
    Does not return anything.
    """
    goodword = getCleanWord(word, d.keys())
    while word and not goodword:
        print(f"{word} is not in the dictonary."   ) 
        word = input("Try again or leave blank to quit, what word? ")
        goodword = getCleanWord(word, d.keys())
    if goodword:
        word = goodword # we don't need the original word anymore.
        printDefinitions(d, word )
        defnum = 0  # remember HUMANS start numbering at 1. Python at 0.
        while defnum == 0:
            defnum_str = input("What definition do you want to update? Type the number.  Blank to exit: ")
            if not defnum_str:
                return
            try:
                defnum = int(defnum_str)
            except:
                defnum = 0
            if defnum > len(d[word]):
                print(f"There are only {len(d[word])} definitions in there.")
                defnum = 0
            else:
                print(f"Selecting definition {defnum}.")
        defnum -= 1 #adjust to python numbering now.
        print("Replacing definition of {word} as: ", d[word][defnum])
        newDefinition = input(f"Type new definition for {word} to replace (or blank to cancel): \n> ")
        if newDefinition: 
            d[word][defnum] = newDefinition


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
            word = input("What word do you want to update a definition for? ")
            updateDefinitionOfWord(d,word)
        elif actionFirst == 'D':
            print("Not ready for that yet.")
        elif actionFirst == 'Q':
            done = True
        else:
            print("Huh? Dude.  Can you READ?")
        


            




