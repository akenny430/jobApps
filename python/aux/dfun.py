import json 
import os

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

    # creating new directory in the base 
    os.system('mkdir ' + pathToBase + '/' + name)

def removeData(name):
    """Function to remove data set"""
    pass


def addInfo():
    """Function to add your personal information to JSON file"""
    pass 

if __name__ == '__main__':
    newData('hey')