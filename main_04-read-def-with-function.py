
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
        word = goodword # we don't need goodword anymore.
        #print(f"{word}  is in there!  Looks like {goodword}")
        definitions = d[word]
        print( ('Definition' if len(definitions) == 1 else 'Definitions'), 'of', word, ': ')
        for i in range(len(definitions)):
            print(f"Definition {i+1}:")
            print(d[word][i])
            print()



d = loadDict()
done = False
while not done:
    word = input("What's the word? Leave blank to quit: ")
    if not word:
        done = True
    else:
        printDefinitions(d, word)
        



            




