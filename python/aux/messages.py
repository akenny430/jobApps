from .colors import colorWrap

def wrapM(input, state=None):
    # inner function to wrap message in specified color
    def _wrapMessage(input, color, character):
        return colorWrap(character, color) + ' ' + input + ' ' + colorWrap(character, color)

    # printing the message
    if state == 's': # success 
        return _wrapMessage(input, 'g1', '%%')
    elif state == 'f': # failure 
        return _wrapMessage(input, 'r', '!!')
    elif state == 'w1': # warning 
        return _wrapMessage(input, 'y', '!!')
    elif state == 'c': # celebration
        return _wrapMessage(input, 'y', '*')
    else: # generic message 
        return _wrapMessage(input, 'dg', '%%')

def printM(input, state=None):
    print(wrapM(input, state))

def _dateCast(input):
    """Function to properly express dates written in '%y%m%d' format"""
    return '20' + input[0:2] + '/' + input[2:4] + '/' + input[4:6]