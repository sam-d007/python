car = {
    "model" : "X7",
    "maker" : "BMW",
    "engine" : "V8",
    "price" : 1000000
}

#accessing values in a dict
print(car["model"])

#iterating over keys:
for key in car.keys():
    print(f"key is {key}")

#iterating over values:
for value in car.values():
    print(f"value is {value}")

#accessing both key and value together:
for key,val in car.items():
    print(f"key is {key} and value is {val}")

#for checking if a key exists in a dictionary
if "price" in car:
    print("Key is present!")


#Dictionary in built methods - d.clear(), d.copy(), d.fromkeys()

user = {}.fromkeys(['name','age','gender'], 'unknown')  #assigning defalut values to all the keys
print('\n')
print(user)

#use get() to check if a key is present, return None if key is not present
print(user.get('name'))
print(user.get('no_key'))

#more methods
#d.pop('key_name') -> remove the item
#d1.update(d2) -> adds d2 dict to d1 dict