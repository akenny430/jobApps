import json 
import os

from .colors import colorWrap
from .messages import printM
from .defaults import defaultJSON as _defaultJSON, defaultFOLDER as _defaultFOLDER





def addCompany(name, id, jFile=_defaultJSON):
    """Function to add a new company"""

    # new dict to add 
    companyDict = {
        id: {
            'name': name, # name of company 
            'total': 0, # total jobs applied for with this company 
            'jobs': {} # list of all jobs for company 
        }
    }

    # reading in JSON 
    with open(jFile, 'r') as file: 
        database = json.load(file)

    # updating dict 
    database['companies'].update(companyDict)
    database['info']['totalCompanies'] += 1

    # clearing terminal 
    # os.system('clear')

    # overwriting JSON file 
    with open(jFile, 'w') as file:
        json.dump(database, file, indent=4)
        printM('Added ' + colorWrap(name, 'o') + ' to database with id ' + colorWrap(id, 'y'))

    # adding folder to directory
    os.system('mkdir ' + _defaultFOLDER + '/' + id)





def removeCompany(id, jFile=_defaultJSON):
    """Function to remove company from database"""

    # reading in JSON file 
    with open(jFile, 'r') as file: 
        database = json.load(file)

    # trying to pop compnay from database 
    popVal = database['companies'].pop(id, None)

    # clearing terminal 
    # os.system('clear')

    # result 
    if popVal is None: 
        printM('No company with id ' + colorWrap(id, 'y') + ' present in database', 'f')
    else: 
        # updating grand total jobs 
        compJobs = 0
        for _ in popVal['jobs']:
            compJobs += 1
        database['info']['totalJobs'] -= compJobs
        database['info']['totalCompanies'] -= 1

        # overwriting JSON file 
        with open(jFile, 'w') as file:
            json.dump(database, file, indent=4)
            printM(
                'Removed ' + colorWrap(popVal['name'], 'o') + ' from database, along with ' + colorWrap(str(compJobs), 'pi') + ' jobs'
            )
        
        # removing folder from directory
        os.system('rm -r ' + _defaultFOLDER + '/' + id)