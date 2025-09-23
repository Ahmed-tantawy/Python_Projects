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
print("=" *50)
print("=" *50)

#----------------------------------------
#---- User Input -----
#----------------------------------------
# input() - All input is string
#----------------------------------------

fname = input("Enter your first name: ")
mname = input("Enter your middle name: ")
lname = input("Enter your last name: ")

fname = fname.strip().capitalize()
mname = mname.strip().capitalize()
lname = lname.strip().capitalize()

print(f"Hello {fname} {mname:.1s} {lname}, welcome to Python programming!")

#----------------------------------------
# --- practice Slice Email-----
#----------------------------------------
print("=" *50)
print("=" *50)

theName = input("what\'s your name? ").strip().capitalize()
theEmail = input("what\'s your email? ").strip().lower()


thename=theName.strip().capitalize()
theUserName= theEmail[:theEmail.index("@")]
theWebsite= theEmail[theEmail.index("@")+1:]

print(f"Hello {theName}, your email is {theEmail}")
print(f"Your Username is {theUserName} \n your email domain is {theWebsite}")


# email = "Jhon_weak@gmail.com"
# print(email[:email.index("@")])

#----------------------------------------
# ----Practical Your Age Full Details-----
#----------------------------------------
print("=" *50)
print("=" *50)
#input Age
theAge = int(input("How old are you? ").strip())

# Get Age in All Time Units
ageMonths = theAge * 12
ageWeeks = theAge * 52
ageDays = theAge * 365
ageHours = ageDays * 24
ageMinutes = ageHours * 60
ageSeconds = ageMinutes * 60

print(f"You Lived for: ")
print(f"{ageMonths} Months")
print(f"{ageWeeks:,} Weeks")
print(f"{ageDays:,} Days")
print(f"{ageHours:,} Hours")
print(f"{ageMinutes:,} Minutes")
print(f"{ageSeconds:,} Seconds")