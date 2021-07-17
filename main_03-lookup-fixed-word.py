
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

word = 'flower'
d = loadDict()
print("The definition(s) of ", word, ': ')
print("\n".join(d[word]))




