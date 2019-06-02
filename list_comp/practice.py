'''
Practicing List comprehensions

[__ for __ in list/range]  -> the blank is for the variables

'''

lc1 = [num**2 for num in range(1,6)]
print("The square of numbers is ", lc1)

name = "ronaldo"
lc2 = [char.upper() for char in name]
print("The modified name is ", lc2)

#using conditional statements with list comprehensions

#if the nunber is even multiply by 2 else divide by 2
lc3 = [num*2 if num % 2 == 0 else num/2 for num in range(1,11)]
print("Conditional LC result ", lc3)

#removing vowels from a string
s1 = "Remove the vowels."
lc4 = [char for char in s1 if char not in "aeiou"]
print("LC after removing vowels : ", lc4)
print("After joining the vowels : ", ''.join(lc4))