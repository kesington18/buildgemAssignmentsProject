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
print(thislist)