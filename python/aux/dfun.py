import json 
import os
# import time 

from .colors import colorWrap
from .messages import printM





def newData(name, email=None, phone=None, GitHub=None, LinkedIn=None, Twitter=None):
    """Function to create a new dataset to start adding jobs to"""

    # getting directory path to the main directory of wherever this project is stored in the system
    pathToBase = os.path.dirname(os.path.realpath(__file__)) + '/../..'

    # creating new JSON file 
    newDict = {
        'info': {
            'email': '' if email is None else email, 
            'phone': '' if phone is None else phone, 
            'GitHub': '' if GitHub is None else GitHub, 
            'LinkedIn': '' if LinkedIn is None else LinkedIn, 
            'Twitter': '' if Twitter is None else Twitter, 
            'totalJobs': 0,
            'totalCompanies': 0
        }, 
        'companies': {}
    }
    with open(pathToBase + '/data/' + name + '.json', 'w') as file: 
        json.dump(newDict, file, indent=4)

    # adding terms to default json 
    defaultDict = {
        name: {
            '_defaultJSON': pathToBase + '/data/' + name + '.json',
            '_defaultFOLDER': pathToBase + '/' + name
        }
    }
    with open(pathToBase + '/data/00-datasets.json', 'r') as file: 
        tempDict = json.load(file)
    tempDict['current'] = name
    tempDict['datasets'].update(defaultDict)
    with open(pathToBase + '/data/00-datasets.json', 'w') as file: 
        json.dump(tempDict, file, indent=4)

    # creating new directory in the base 
    os.system('mkdir ' + pathToBase + '/' + name)

    # printing message 
    printM('Added new database called ' + colorWrap(name, 'r'))





def removeData(name, newDefault=None):
    """Function to remove data set"""

    # getting directory path to the main directory of wherever this project is stored in the system
    pathToBase = os.path.dirname(os.path.realpath(__file__)) + '/../..'

    # removing both the folder and JSON 
    os.system('rm -rf ' + pathToBase + '/' + name)
    os.system('rm -f ' + pathToBase + '/data/' + name + '.json')

    # removing from database json 
    with open(pathToBase + '/data/00-datasets.json', 'r') as file: 
        tempDict = json.load(file)
    tempDict['datasets'].pop(name, None) 
    if newDefault is None: 
        tempDict['current'] = '' if len(tempDict['defaults']) == 0 else [*tempDict][0]
    else:
        tempDict['current'] = newDefault
    with open(pathToBase + '/data/00-datasets.json', 'w') as file: 
        json.dump(tempDict, file, indent=4)

    # printing message 
    printM('Removed database ' + colorWrap(name, 'r'))





# if __name__ == '__main__':
#     newData('hey', email='blah@blah.com')
#     time.sleep(10)
#     removeData('hey', '22')