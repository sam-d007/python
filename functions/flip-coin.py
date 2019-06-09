from random import random

def flip_coin():
    number = random()
    call = float(number)
    if call > 0.5:
        return "Heads"
    else:
        return "Tails"   

result = flip_coin()
print(result)        


def know(parameter1, parameter2):  #These are the parameters
    return parameter1,parameter2

know("arg1","arg2") #These are the arguments