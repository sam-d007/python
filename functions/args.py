def sum(*args):
    '''The *args parameter is a special parameter that can take multiple arguments and store it in a tuple'''
    print(args)
    sum=0
    for num in args:
        sum+=num
    return sum

sum1 = sum(5,10,15,20) 
print(sum1)

#unpacking tuple
v = (10,20,30,40,50)

s2 = sum(*v)
print(s2)