import secrets
import string

minus = "abcdefghijklmnñopqrstuvwxyz"
mayus = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
nums = string.digits
simb = string.punctuation

def generator(nchars, opts):
    alphabet = ''
    pwd = ''
    nchars = int(nchars)

    if 'min' in opts:
        alphabet = alphabet+minus
    if 'may' in opts:
        alphabet = alphabet+mayus
    if 'num' in opts:
        alphabet = alphabet+nums
    if 'sim' in opts:
        alphabet = alphabet+simb
    
    for i in range(nchars):
        pwd = pwd + secrets.choice(alphabet)

    return pwd
