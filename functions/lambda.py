#lambdas are short hand function notations
# Syntax - lambda "parameters" : "single expression"  #the expression is automatically returned

def square(num):
    return num*num

print(square(7))  


square2 = lambda num : num*num  #A short way to write the above function
print(square2(7))