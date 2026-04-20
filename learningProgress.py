# list
thislist = ["apple", "banana", "cherry"]

# inserting in a list
thislist[0] = "banana"
thislist.insert(2, "corn")

# To append elements from another list to the current list, use the extend() method.
tropical = ["mango", "pineapple", "papaya"]
thistuple = ("kiwi", "orange")
thislist.extend(tropical)
thislist.extend(thistuple)

# The remove() method removes the specified item.
thislist.remove("mango")
# The pop() method removes the specified index.
thislist.pop(2)
thislist.pop() # If you do not specify the index, the pop() method removes the last item.
del thislist[0]
# del thislist # this deletes the entirely list
# thislist.clear() # The list still remains, but it has no content.
# print(thislist)

# A short hand for loop that will print all items in a list:
# [print(x) for x in thislist]
# The Syntax
# newlist = [expression for item in iterable if condition == True]
# newlist = [x for x in thislist if "a" in x]
# newlist = [x for x in thislist]
newlist = [x if x != "banana" else "orange" for x in thislist]
print(newlist)