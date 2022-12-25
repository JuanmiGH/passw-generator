import secrets
import string
import re

minus = "abcdefghijklmnñopqrstuvwxyz"
mayus = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
nums = string.digits
simb = '!#$%&()*+,-.:;<=>?@^_`|~'

def generator(nchars, opts):

    alphabet = ''
    nchars = int(nchars)

    if 'min' in opts:
        alphabet = alphabet+minus
    if 'may' in opts:
        alphabet = alphabet+mayus
    if 'num' in opts:
        alphabet = alphabet+nums
    if 'sim' in opts:
        alphabet = alphabet+simb
    
    for c in range(100):
        pwd = ''
        strengh = 0.0
        for i in range(nchars):
            pwd = pwd + secrets.choice(alphabet)

        if 'min' in opts and bool(re.search(r'[a-z]', pwd)) == False:
            minValid = False
        else:
            strengh += 0.5
            minValid = True

        if 'may' in opts and bool(re.search(r'[A-Z]', pwd)) == False:
            mayValid = False
        else:
            strengh += 0.5
            mayValid = True

        if 'num' in opts and bool(re.search(r'[0-9]', pwd)) == False:
            numValid = False
        else:
            strengh += 0.5
            numValid = True

        if 'sim' in opts and bool(re.search(r'[!#$%&()*+,-.:;<=>?@^_`|~]', pwd)) == False:
            simValid = False
        else:
            strengh += 0.5
            simValid = True
        
        if minValid and mayValid and numValid and simValid == True:
            valid = True
            strengh += nchars
            print(strengh)
            break
        
        
    if valid == True:
        return [pwd, strengh]
    else:
        return ['P4$$w0rD', '', 'Less conditions or more characters needed']
