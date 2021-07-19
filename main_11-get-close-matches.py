
# Hello!  This is our first big project!



"""

In this version, I'm adding the ability of "
You typed woord.  Did you mean 'word' ?

Note the import function at top

All I had to do was make one function (get close match) and edit the input_word function!

"""
import json
from difflib import get_close_matches

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


def input_closeMatch(word, wordlist):
    bestMatchList = get_close_matches(word,wordlist,n=4,cutoff=0.8)
    if len(bestMatchList) == 0:
        # No close matches.
        return None
    print("Close matches are: ")
    for closeone in bestMatchList:
        print(f"  {closeone}")
    answer = input(f"Did you mean {bestMatchList[0]}?  ").lower()
    if answer and answer[0] == 'y':
        return bestMatchList[0]
    return None


def input_word(wlist, prompt, reprompt = True, existing=True):
    """ see if the word w is in the list wlist. 
    if exising, then we are looking for a word already in the list of words.
        Otherwise, we are looking for a word NOT already in the list of words.
        
    If we find a word (either existing or not), return that.  
    But if reprompt is set and we don't find a word, reprompt.

    If not there and no reprompt or the user wants to cancel, return None """
    
    done = False
    goodword = None  # this is the default return value.
    while not done:
        word = input(prompt)
        if existing:
            goodword = getCleanWord(word, wlist)
            if not goodword:
                goodword = input_closeMatch(word, d.keys())
        else: 
            # we want a NEW word that is not in there, exactly as given.
            goodword = None if word in wlist else word
        if not goodword:
            print(f"{word} is {'not' if existing else ''} in the dictonary."   ) 
            if not reprompt:
                done = True
        else:
            done = True
    return goodword


def input_definitionNumber(d, word, prompt, allowAdd = False):
    """ Let's input and return the definition number for a word.
    Return None if the user wants to cancel.
    Note that both None and 0 are Falsey - so have to use xxxx is None to test that.
    """
    defnum = None # remember HUMANS start numbering at 1. Python at 0.
    done = False
    while not done:
        defnum_str = input(f"{prompt}.  Blank to exit: ")
        if not defnum_str:
            done = True
        try:
            defnum = int(defnum_str)
        except:
            pass
        if defnum is None:
            print("Hmmm?  Didn't understand.")
        elif defnum <= 0:
            print("Dude.  How about something positive.")
        elif defnum > len(d[word]):
            print(f"There are only {len(d[word])} definitions in there.")
            defnum = None # keep going
        else:
            print(f"Selecting definition {defnum}.")
            done = True
    return (None if defnum is None else defnum - 1)  # correct for python numbering.


def test_input_definitionNumber(d):

    done = False
    testword = 'lead'
    printDefinitions(d, testword)
    while not done:
        dnum = input_definitionNumber(d,testword,f'Which definition of {testword}? ')
        if dnum is None:
            done = True
        else:
            print("Definition {dnum} is:")
            print(d[testword][dnum])
    

def printDefinitions(d, word):
    """ prints the definitions of a word, or prints a message if not present. 
    No side effects - does not change the dictionary.
    Does not return anything.
    """
    #print(f"{word}  is in there!  Looks like {goodword}")
    if word in d:
        definitions = d[word]
        print( ('Definition' if len(definitions) == 1 else 'Definitions'), 'of', word, ': ')
        for i in range(len(definitions)):
            print(f"Definition {i+1}:")
            print(d[word][i])
            print()
    else:
        print(f"Word {word} is not in the dictionary.")


def updateDefinitionOfWord(d, word):
    """ updates a definition of a word.
    Can add a new definition for a word too.

    Does not return anything.
    """
    printDefinitions(d, word)
    if len(d[word]) == 0:
        # No point asking which definition number, there aren't any definitions
        defnum = None
    else:
        addWord = (input("Do you want to add a new definition?  Yes or no?")).lower()
        if addWord and addWord[0] == 'y':
            print(f"Adding a definition for {word}")
            defnum = None
        else:
            defnum = input_definitionNumber(d, word, "What definition do you want to update?")
            print(f"Replacing definition of {word} as: \n{d[word][defnum]}")

    newDefinition = input(f"Type new definition for {word}: \n> ")
    if newDefinition: 
        if defnum is None:
            d[word].append(newDefinition)
        else:
            d[word][defnum] = newDefinition
    printDefinitions(d, word)


def deleteDefinitionOfWord(d, word):
    """ deletes the definitions of a word, and deletes the word from the dictionary if it's the last definition. 
    """
    printDefinitions(d, word )
    defnum = input_definitionNumber(d, word, "What definition do you want to delete?")
    del d[word][defnum]
    if len(d[word]) == 0:
        print(f"That was the last definition for {word} - Removing.")
        del d[word]
    printDefinitions(d, word)


def inputAndAddNewWord(d, w):
    # Let's add a word with no definitions
    d[w] = []
    updateDefinitionOfWord(d,w)
    printDefinitions(d,w)


#
#  Here we implement the main menu.
#

d = loadDict()

# I use this to test out some code....
testing = False

if testing:
    test_input_definitionNumber(d)
    print("Testing is done... now we're gonna go to the main loop.")


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
            word = input_word(d.keys(), "What's the new word? ", existing=False)
            if word:
                inputAndAddNewWord(d, word)

        elif actionFirst == 'R':
            word = input_word(d.keys(), "What's the word you want to look up? ", reprompt = False)
            if word:
                printDefinitions(d, word)
        elif actionFirst == 'U':
            word = input_word(d.keys(), "What's the word you want to update? ")
            if word:
                updateDefinitionOfWord(d,word)
        elif actionFirst == 'D':
            word = input_word(d.keys(), "What word do you want to delete a definition for? ")
            if word:
                deleteDefinitionOfWord(d,word)
        elif actionFirst == 'Q':
            done = True
        else:
            print("Huh? Dude.  Can you READ?")
        


            




