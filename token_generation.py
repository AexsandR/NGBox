import random
import string

def genaration_token(lenght):
    symbols = string.digits + string.ascii_lowercase
    token = ""
    for i in range(lenght):
        token += random.choice(symbols)
    return token


