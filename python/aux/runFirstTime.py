import json 
import os 

from .colors import colorWrap
from .messages import printM, wrapM

# getting directory path to the main directory of wherever this project is stored in the system
pathToBase = os.path.dirname(os.path.realpath(__file__))[:-11]

def createAll():
    """Function to run for the first time """

    # checking to see if file already exists 
    if os.path.exists(pathToBase + '/data/00-datasets.json'):
        print(wrapM("Initialization has already taken place", 'f'))
        return 

    # original dataset 
    originalDict = {
        'current': '',
        'datasets': {}
    }

    # turning dictionary to json 
    with open(pathToBase + '/data/00-datasets.json', 'w') as file:
        json.dump(originalDict, file, indent=4)
    return 