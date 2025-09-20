#---------------
#----list-----
#----------

#append() 

myFreuits = ['apple', 'banana', 'cherry']
myFreuits.append('orange')
print(myFreuits)
myFreuits.append(1000)
myOldFreuits = ['grape', 'mango', 'papaya']
myFreuits.append(True)
myFreuits.append(myOldFreuits)
print(myFreuits)

print(myFreuits[6][2])

#extend() - Add elements of a list (or any iterable), to the end of the current list
a = [1, 2, 3]
b= ["a", "b", "c"]
c= [100, 200, 300]
a.extend(b)
a.remove("c")
print(a)

#sort() - Sort the list ascending by default oteroptionally use reeverse=True for descending order
y= [100, 50, 65, 82, 23]
x = ['banana', 'Orange', 'Kiwi', 'cherry']
y.sort()
print(y)
y.sort(reverse=True)
print(y)

# reverse() - Reverse the order of the list
print(y.reverse())

#claer() - Remove all the elements from a list
q = [100, 50, 65, 82, 23]
a.clear()
print(a)
w = [22,33,44,55]
# copy() - Return a copy of the list
e = w.copy()
print(e)

#count()
d = [1, 2, 3, 4, 1, 2, 1, 1, 1]
print(d.count(1))

#index()

xs = ['banana', 'Orange', 'Kiwi', 'cherry']
print(xs.index('Kiwi'))

#insert() - Insert an item at the specified index
xsa = ['banana', 'Orange', 'Kiwi', 'cherry']
xsa.insert(len(xsa), 'apple')
xsa.insert(1, 'grape')
print(xsa)

#pop() - Remove the element at the specified position
xsp = ['banana', 'Orange', 'Kiwi', 'cherry', 123, 456]
xsp.pop(-1) #removes the last element
print(xsp)

#---------------------------------------
#----Tuples-----
# [1] Tuple items are Enclosed in paranthesis ()
# [2] You can Remove items using del keyword
# [3] Tuples are ordered, unchangeable, and allow duplicate values
# [4] Operators: +, *, in, not in can be used with tuples, lists,  strings
# [5]
#---------------------------------------

myAwesomeTuple = ('apple', 'banana', 'cherry', 'apple', 'cherry')
myAwesomeTuple2 = (1, 5, 7, 9, 3)
myAwesomeTuple3 = (True, False, False)
print(myAwesomeTuple)
print(type(myAwesomeTuple))

# Tup;le Indexing 

print(myAwesomeTuple2[2])
print(myAwesomeTuple2[0:])
# myAwesomeTuple [2] = "orange" #Tuples are unchangeable, and you cannot change, add or remove items once the tuple is created   
# print(myAwesomeTuple)    

# Tuple itemes
myAwesomeTuple5 = ('apple', 'apple', 'cherry', 323,4345, True, False, 3.14)
print(len(myAwesomeTuple5))
print(myAwesomeTuple5[-1])
print(myAwesomeTuple5[1])

myString = "Hello, World!"
myList = [3,4,5,6]
myTuple = (7,8,9)
print(myString * 4)
print(myList * 4)
print(myTuple * 4)

# method count()
aa = (1, 2, 3, 4, 1, 2, 1, 1)
print(aa.count(1))
# method index()
bbb = (12,34,56,78,90)
print(f"The position of 3 in the tuple is: {aa.index(3)}")

# tuple Destruct

aaaa = ("A", "B", 43,"C")
x, y, _,z = aaaa
print(x)
print(y)
print(z)

# ------------------------
# ----Set-----
#------------------------
# [1] Set items are Enclosed in curly brackets {}
# [2] NOt ordered nor indexed
# [3] Sets are unordered, unchangeable*, and do not allow duplicate values
# [4] not sliceing and indexing


mySet = {"apple", "banana", "cherry"}
print(mySet)
print(type(mySet))

# print(mySet[0])
# not sliceing and indexing
# print(mySet[0:3])

# Has only immutable data types
# mySet2 = {"apple", "banana", "cherry", 1, 3.14, True, (1,2,3)}
# print(mySet2)

#items are Unique
mySet4 = {1, 2, "apple", "one", "apple", 2}
print(mySet4)

# set methods
# add() - Add an item to a set, if the item already exists, the set will not change
mySet5 = {"apple", "banana", "cherry"}
mySet5.add("orange")
print(mySet5)

# clear() - Remove all items from the set
mySet5.clear()
print(mySet5)
# union() - Return a set that contains all items from both sets, duplicates are excluded
setA = {"a", "b", "c"}
setB = {1, 2, 3}
setC = setA.union(setB, {4,5,6})
print(setC)
print (setA | setC)

# add()

setD= {"apple", "banana", "cherry"}
setD.add("orange")
print(setD)

# copy() - Return a copy of the set

setE = {1, 2, 3, 4, 5}
setF = setE.copy()
print(setF)
print(setE)

setE.add(6)
print(setE)
print(setF)

# remove() - Remove the specified item
setG = {1,2,3,4,5}
g.remove(3)
print(g)
# remove(7)

# discard() - Remove the specified item, if the item does not exist, do nothing
setH = {1,2,3,4,5}
setH.discard(10) #discard does not raise an error
print(setH)

