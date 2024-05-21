#list
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, "eighteen", 2)
mydict = {"one" : 1, "two" : 11}
print(mylist[2])
print(mytuple[1])
print(mydict["two"]) # dictionaries are accessed via keys

mylist.append(7) # append() if you want to add an element to the end of the list.
mylist.insert(3, 6) # insert(index,value) if you want to add an element at a specific position in the list.
print(mylist)
print(mylist[0:6:2]) # use slices to get parts of a sequence
print(mylist[::-1]) # you can use slices to reverse a sequence
