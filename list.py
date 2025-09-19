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

# tuple 