#A map function needs two arguments: a function and an iterable(list, tuples, dictionaries)

sl = [2, 3, 5, 7, 9] # we want to have the square of every element in the list

res = list(map(lambda x: x*x ,sl))
print(res)

names = ["Sam", "Ronaldo", "Hazard"]

res2 = list(map(lambda name: name.upper(),names)) #convert the name list ot uppercase
print(res2)