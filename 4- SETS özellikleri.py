thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
print("-------------")

thisset = {"apple", "banana", "cherry"}

print(len(thisset))
print("-------------")

set1 = {"abc", 34, True, 40, "male"}
print("-------------")


myset = {"apple", "banana", "cherry"}
print(type(myset))
print("-------------")


thisset = set(("apple", "banana", "cherry"))
# note the double round-brackets
print(thisset)
print("-------------")


thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
print("-------------")

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
print("-------------")


thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
print("-------------")


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
print("-------------")



thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)
print("-------------")

#Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
print("-------------")

#Remove "banana" by using the discard() method
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
print("-------------")


#Remove the last item by using the pop() method:
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)
print(thisset)
print("-------------")


#The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)
print("-------------")


#The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)
print("-------------")


#Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

print("-------------")


#The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
print("-------------")


#The update() method inserts the items in set2 into set1:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
print("-------------")

