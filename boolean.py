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