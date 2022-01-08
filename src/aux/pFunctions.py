import json 
import os

from .colors import colorWrap, colorPrint
from .messages import wrapM
from .defaults import defaultJSON as _defaultJSON


def printInfo(cid=None, level=None, personal=False, jFile=_defaultJSON):
    "Function to print out specific info about certain companies"

    # aux function to print out the correct color of the job status
    def _wrapStatus(input):
        if input == 'W':
            return colorWrap('W', 'y')
        elif input == 'R':
            return colorWrap('R', 'r')
        elif input == 'O':
            return colorWrap('O', 'b1')
        elif input == 'A':
            return wrapM(colorWrap('A', 'b1'), 'c')
        else:
            return colorWrap('?', 'dg')

    # reading in JSON file 
    with open(jFile, 'r') as file: 
        database = json.load(file)

    # clearing out rest of terminal
    os.system('clear')

    # printing out personal info
    if personal is True: 
        tempCol = 'lg'
        print('=' * 50 + '\n')
        print(colorWrap('Email:    ', tempCol) + database['info']['email'])
        print(colorWrap('Phone:    ', tempCol) + database['info']['phone'])
        print(colorWrap('GitHub:   ', tempCol) + database['info']['GitHub'])
        print(colorWrap('LinkedIn: ', tempCol) + database['info']['LinkedIn'])
        print(colorWrap('Twitter:  ', tempCol) + database['info']['Twitter'])
        print('\n' + '=' * 50)
        return 

    # if no company is specified, print out all of the info from all of the companies
    if cid is None:
        # making default level in this case 
        if level is None: 
            level = 3

        # printing total number of jobs applied to 
        print('=' * 50)
        print('Applied to ' + colorWrap(str(database['info']['totalJobs']), 'pi') + ' jobs at ' + colorWrap(str(database['info']['totalCompanies']), 'pu') + ' companies')
        print('-' * 50 + '\n')

        if level == 1: # print out companies only
            for companies, companyInfo in database['companies'].items():
                print('(' + colorWrap(companies, 'o') + '): ' + companyInfo['name'])
            print('\n' + '=' * 50)
        else: # could have more
            for companies, companyInfo in database['companies'].items():
                print('(' + colorWrap(companies, 'o') + '): ' + companyInfo['name'])
                if level == 2: # print out companies and jobs only
                    colorPrint('%%', 'dg')
                    for jobs, jobInfo in companyInfo['jobs'].items():
                        print('(' + colorWrap(jobs, 'g1') + '): ' + jobInfo['title'] + ', ' + _wrapStatus(jobInfo['status']))
                else: # have full specification
                    colorPrint('%%', 'dg')
                    for jobs, jobInfo in companyInfo['jobs'].items():
                        print('(' + colorWrap(jobs, 'g1') + '): ' + jobInfo['title'] + ', ' + _wrapStatus(jobInfo['status']))
                        for tag, message in jobInfo['notes'].items():
                            colorPrint('      ' + tag + ': ' + message, 'mg')
                        colorPrint('%%', 'dg')
                print('\n') # new space after every company
            print('=' * 50)
        return 

    # otherwise, print out all of the jobs and updates from specific company
    # making default level 1
    if level is None:
        level = 1
    compDict = database['companies'][cid]
    print('=' * 50 + '\n')
    print('(' + colorWrap(cid, 'o') + '): ' + compDict['name'])
    if level == 1: # print out companies and jobs only
        colorPrint('%%', 'dg')
        for jobs, jobInfo in compDict['jobs'].items():
            print('(' + colorWrap(jobs, 'g1') + '): ' + jobInfo['title'] + ', ' + _wrapStatus(jobInfo['status']))
    else: # have full specification
        colorPrint('%%', 'dg')
        for jobs, jobInfo in compDict['jobs'].items():
            print('(' + colorWrap(jobs, 'g1') + '): ' + jobInfo['title'] + ', ' + _wrapStatus(jobInfo['status']))
            for tag, message in jobInfo['notes'].items():
                colorPrint('      ' + tag + ': ' + message, 'mg')
            colorPrint('%%', 'dg')
    print('\n' + '=' * 50)