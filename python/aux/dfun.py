import json
import os
# import time 

from .colors import colorWrap
from .messages import printM

# getting directory path to the main directory of wherever this project is stored in the system
pathToBase = os.path.dirname(os.path.realpath(__file__))[:-11]





def _readjustInfo():
    """Aux function to have the default JSON file printed in info.py file"""

    # getting all datasets along with current one
    with open(pathToBase + '/data/00-datasets.json', 'r') as file: 
        tempDict = json.load(file)
    current = tempDict['current']

    # writing defaults 
    with open(pathToBase + '/python/aux/info.py', 'w') as file:
        for names, defaults in tempDict['datasets'].items():
            if names == current:
                file.write(f"_defaultJSON = '{defaults['_defaultJSON']}'\n")
                file.write(f"_defaultFOLDER = '{defaults['_defaultFOLDER']}'\n")







def newData(name, email=None, phone=None, GitHub=None, LinkedIn=None, Twitter=None):
    """Function to create a new dataset to start adding jobs to"""

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

    # readjusting default database 
    _readjustInfo()





def removeData(name, newDefault=None):
    """Function to remove data set"""

    # removing both the folder and JSON 
    os.system('rm -rf ' + pathToBase + '/' + name)
    os.system('rm -f ' + pathToBase + '/data/' + name + '.json')

    # removing from database json 
    with open(pathToBase + '/data/00-datasets.json', 'r') as file: 
        tempDict = json.load(file)
    tempDict['datasets'].pop(name, None) 
    # having to change current directory if it is set to the one we are deleting 
    if tempDict['current'] != name: 
        pass
    else: 
        if newDefault is None: 
            tempDict['current'] = '' if len(tempDict['datasets']) == 0 else [*tempDict['datasets']][0]
        else:
            tempDict['current'] = newDefault
    with open(pathToBase + '/data/00-datasets.json', 'w') as file: 
        json.dump(tempDict, file, indent=4)

    # printing message 
    printM('Removed database ' + colorWrap(name, 'r'))

    # readjusting default database 
    _readjustInfo()





def selectData(name):
    """Function to select current dataset from multiple"""

    # reading in dataset json 
    with open(pathToBase + '/data/00-datasets.json', 'r') as file: 
        tempDict = json.load(file)
    if name in tempDict['datasets']:
        tempDict['current'] = name 
        with open(pathToBase + '/data/00-datasets.json', 'w') as file: 
            json.dump(tempDict, file, indent=4)
        printM('Changed current dataset to ' + colorWrap(tempDict['current'], 'r'))
    else: 
        printM('The dataset you are trying to select is not in the json file')
        allData = ''
        for dataNames in tempDict['datasets']:
            allData += dataNames + ', '
        printM('The current datasets are ' + allData[:-1])





# if __name__ == '__main__':
#     newData('hey', email='blah@blah.com')
#     time.sleep(10)
#     removeData('hey', '22')