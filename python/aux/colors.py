# colors taken from 
# https://en.wikipedia.org/wiki/ANSI_escape_code
# format is '\033[38;5;<COLOR>m' + input + '\033[0m'

# aux function to wrap text in certain color
def colorWrap(input, color=None):
    if color == 'r': # red 
        return '\033[38;5;167m' + input + '\033[0m'
    elif color == 'o': # orange 
        return '\033[38;5;178m' + input + '\033[0m'
    elif color == 'y': # yellow 
        # return '\033[38;5;220m' + input + '\033[0m'
        return '\033[38;5;226m' + input + '\033[0m'
    elif color == 'g1': # green 1
        return '\033[38;5;70m' + input + '\033[0m'
    elif color == 'g2': # green 2
        return '\033[38;5;106m' + input + '\033[0m'
    elif color == 'b1': # dark blue
        return '\033[38;5;33m' + input + '\033[0m'
    elif color == 'b2': # light blue
        return '\033[38;5;51m' + input + '\033[0m'
    elif color == 'pu': # purple 
        return '\033[38;5;171m' + input + '\033[0m'
    elif color == 'pi': # pink 
        return '\033[38;5;213m' + input + '\033[0m'
    elif color == 'dg': # dark grey 
        return '\033[38;5;236m' + input + '\033[0m'
    elif color == 'mg': # medium grey 
        return '\033[38;5;239m' + input + '\033[0m'
    elif color == 'lg': # light grey 
        return '\033[38;5;242m' + input + '\033[0m'
    else:
        return input



# aux function to print text in certain color
def colorPrint(input, color=None):
    print(colorWrap(input, color))



# aux function to print a message with comments on the outside, so it is easier to distinguish as "mine"
def cMessage(input, color='dg'):
    return colorWrap('/* ', color) + input + colorWrap(' */', color)