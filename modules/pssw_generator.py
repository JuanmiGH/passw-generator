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

        for i in range(nchars):
            pwd = pwd + secrets.choice(alphabet)

        if 'min' in opts and bool(re.search(r'[a-z]', pwd)) == False:
            minValid = False
        else:
            minValid = True

        if 'may' in opts and bool(re.search(r'[A-Z]', pwd)) == False:
            mayValid = False
        else:
            mayValid = True

        if 'num' in opts and bool(re.search(r'[0-9]', pwd)) == False:
            numValid = False
        else:
            numValid = True

        if 'sim' in opts and bool(re.search(r'[!#$%&()*+,-.:;<=>?@^_`|~]', pwd)) == False:
            simValid = False
        else:
            simValid = True

        if minValid and mayValid and numValid and simValid == True:
            valid = True
            break
        
    if valid == True:
        return [pwd]
    else:
        return ['P4$$w0rD', 'Se necesitan más caracteres o menos condiciones.']
