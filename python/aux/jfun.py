import json 
import os
from datetime import datetime

from .colors import colorWrap
from .messages import printM, _dateCast
from .info import _defaultJSON, _defaultFOLDER





def addJob(id, job, jobTag= None, date=None, updates=0, jFile=_defaultJSON):
    """Function to add job for specific company to database"""

    # reading in JSON file 
    with open(jFile, 'r') as file: 
        database = json.load(file)
    
    # adding default job tag if none is supplied, default is 
    if jobTag is None: 
        jobTag = str(database['companies'][id]['total'] + 1).zfill(2)

    # creating date if none is supplied 
    if date is None:
        date = datetime.now().strftime('%y%m%d')

    # creating dict for job 
    jobDict = {
        jobTag: {
            'title': job, # name of job 
            'date': date, # date applied to job 
            'updates': updates, # number of updates
            'notes': {
                '00': 'applied, ' + _dateCast(date)
            }, # notes that can be updated after every step 
            'status': 'W' # status of job, choices are W (waiting), R (rejected), O (offer), A (accepted)
        }
    }

    # updating dict 
    database['companies'][id]['jobs'].update(jobDict)
    database['companies'][id]['total'] += 1
    database['info']['totalJobs'] += 1

    # overwriting JSON file 
    with open(jFile, 'w') as file: 
        json.dump(database, file, indent=4)
        printM('Added ' + colorWrap(job, 'g1') + ' at ' + colorWrap(id, 'y') + ' on ' + _dateCast(date))
    
    # adding folder to directory
    os.system('mkdir ' + _defaultFOLDER + '/' + id + '/files' + jobTag)





def removeJob(cid, jid, jFile=_defaultJSON):
    """Function to remove job that was applied to at specified company"""

    # reading in JSON file 
    with open(jFile, 'r') as file:
        database = json.load(file)

    # trying to remove job from database 
    popVal = database['companies'][cid]['jobs'].pop(jid, None)

    # result 
    if popVal is None: 
        printM(
            colorWrap(database['companies'][cid]['name'], 'o') + ' has no job with id ' + colorWrap(jid, 'g1') + ' present in database', 
            'f'
        )
    else: 
        # updating grand total and company total
        database['companies'][cid]['total'] -= 1
        database['info']['totalJobs'] -= 1
        # overwriting JSON file
        with open(jFile, 'w') as file:
            json.dump(database, file, indent=4)
        printM(
            'Removed ' + colorWrap(popVal['title'], 'g1') + ' for ' + colorWrap(database['companies'][cid]['name'], 'o') + ' from database'
        )

        # removing folder from directory 
        os.system('rm -r ' + _defaultFOLDER + '/' + cid + '/files' + jid)





def updateJob(cid, jid, message, changeStatus=None, date=None, jFile=_defaultJSON):
    """Function to give update about job"""

    # reading in JSON file 
    with open(jFile, 'r') as file: 
        database = json.load(file)

    # making date if none is given 
    if date is None:
        date = datetime.now().strftime('%y%m%d')


    # adding message 
    updateTag = str(database['companies'][cid]['jobs'][jid]['updates'] + 1).zfill(2)
    database['companies'][cid]['jobs'][jid]['updates'] += 1
    updateDict = {
        updateTag: message + ', ' + _dateCast(date)
    } 
    database['companies'][cid]['jobs'][jid]['notes'].update(updateDict)

    # updating status if it needs to be changed 
    if changeStatus == 'r':
        database['companies'][cid]['jobs'][jid]['status'] = 'R'
    elif changeStatus == 'o':
        database['companies'][cid]['jobs'][jid]['status'] = 'O'
    elif changeStatus == 'a':
        database['companies'][cid]['jobs'][jid]['status'] = 'A'
    elif changeStatus == 'w':
        database['companies'][cid]['jobs'][jid]['status'] = 'W'

    # overwriting JSON file 
    with open(jFile, 'w') as file:
        json.dump(database, file, indent=4)

	# printing message 
    printM(
		'Added update to ' + colorWrap(jid, 'g1') + ' for ' + colorWrap(cid, 'o') + ' to database'
	)
