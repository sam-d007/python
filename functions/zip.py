#Zip is an inbuilt function that is used to aggregate elements from each of the iterables(lists, dicts etc)
#The length of both the iterables must be the same

l1 = [1,3,5,7]
l2 = [2,4,6,8]

zipped = zip(l1,l2)

print(list(zip(l1,l2))) #the order of the arguments also matters
print(dict(zip(l1,l2)))

#To unpack the zipped list to original list use *

unpacked_zip = list(zip(*zipped))
print("unpacked zip ", unpacked_zip)