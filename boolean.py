print (100 > 100  or 100 == 100)
print (100 > 100  and 100 == 100)
print (not(100 > 100  and 100 == 100))  
print("=" *50)
# True Values
print (bool("Hello"))
print (bool(123))
print (bool(["apple", "cherry", "banana"]))
print (bool(3.14))
print (bool(True))
print (bool(1))
print("=" *50)
# False Values
print (bool(False))
print (bool(None))
print (bool(0))
print (bool(""))
print (bool([]))
print (bool(()))
print (bool({}))


#---------------------------------------
#----Boolean Operators-----
#---------------------------------------
# and
# or
# not
#---------------------------------------
age = 36
country = "USA"
if age > 18 and country == "USA":
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# or
if age > 18 or country == "USA":
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# not
if not age > 18:
    print("You are not eligible to vote")
else:
    print("You are eligible to vote")

#---------------------------------------
#----Assignment Operators-----
#---------------------------------------
# =, +=, -=, *=, /=, %=, //=, **=
#---------------------------------------

name = "John"
surname = "Doe"
print(name == surname)  
print(name != surname)
print(name > surname)
print(name < surname)

#---------------------------------------
#----Type Conversion-----
#---------------------------------------
# int(), float(), str(), bool()
#---------------------------------------
# str
a = 10
print(type(a))
print(type(str(a)))

#  list
c = "jhon" #string
d =(1,2,3,4,5) #tuple
e ={"A", "B", "C"} #set
f = {"A":1, "B":2} #dict

print(list(c))
print(list(d))
print(list(e))
print(list(f))

# tuple
c = "jhon" #string
d =[1,2,3,4,5] #list
e ={"A", "B", "C"} #set
f = {"A":1, "B":2} #dict

print(tuple(c))
print(tuple(d))
print(tuple(e))
print(tuple(f))

# set
c = "jhon" #string
d =[1,2,3,4,5] #list
e =("A", "B", "C") #tuple
f = {"A":1, "B":2} #dict

print(set(c))
print(set(d))
print(set(e))
print(set(f))

# dict

# c = "jhon" #string
d =[[1, "one"],[2, "two"], [3, "three"]] #list
e =(("A", 1), ("B", 2), ("C", 3)) #set
# f = {"A", "B"} #set unhashable type

# print(dict(c))
print(dict(d))
print(dict(e))
# print(dict(f))