import json 

with open('aux/info.json', 'r') as file: 
    defaultInfo = json.load(file)

defaultJSON = defaultInfo['defaultJSON']
defaultFOLDER = defaultInfo['defaultFOLDER']


# if __name__ == '__main__':
#     print('Default JSON: ' + _defaultJSON)