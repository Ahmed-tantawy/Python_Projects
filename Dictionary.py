#-----------------------------------------
# ----Dictionary-----
#-----------------------------------------
# [1] Dictionary items are enclosed in curly brackets {}
# [2] Dictionary items are presented in key:value pairs
# [3] Dictionary is ordered, changeable, and does not allow duplicates
# [4] Dictionary items are indexed, the first item has index [0], the second

# Dictionary

user = {
    "name": "Ahmed",
    "age": 25,
    "Country": "Egypt",
    "skills": ["HTML", "CSS", "JavaScript", "Python"],
    "rating": 10.5,
    "name": "Ali"  # Duplicate key, the last one will be used
   }

print(user['Country'])
print(user.get("Country"))
print(user.keys())
print(user.values())

# two-Dimensional dictionary
languages = {
    "one": {
        "name": "HTML",
        "progress": "80%"
    },
    "two": {
        "name": "CSS",
        "progress": "70%"
    },
    "three": {
        "name": "JavaScript",
        "progress": "60%" 
    }
}

print(languages)
print(languages["one"]["progress"])
# Dictionary Length
print(len(languages["two"]))

# create dictionary from variables
frameworkOne = {
    "name": "Vuejs",
    "progress": "80%"
}
frameworkTwo = {
    "name": "Reactjs",
    "progress": "70%"
}
frameworkThree = {
    "name": "Angular",
    "progress": "60%"
}
# store frameworks in one dictionary
allFrameworks = {
    "one": frameworkOne,
    "two": frameworkTwo,
    "three": frameworkThree
}
print(allFrameworks)
print("*" * 40)
print(len(allFrameworks["one"]))
#----------------------------------------------
# Dictionary Methods
#----------------------------------------------


print(user)
# clear() - Empties the dictionary
user.clear()
print(user)

print("*" * 50)

# update() - Updates the dictionary with the specified key-value pairs

member = {
    "name": "Ahmed",
    "age": 25,
    "Country": "Egypt"
}

print(member)
member.update({"Age": 26})
member.update({"age": 26})
print(member)

# copy() - Returns a copy of the dictionary

mainMember = {
    "name": "Ahmed",
    "age": 25,
    "Country": "Egypt"
    }
print(mainMember)
newMember = mainMember.copy()
print("*" * 50)
print(newMember)
mainMember.update({"test": 26})
print(mainMember)
print(newMember)

# keys() + values() - Returns a list of all the keys or values in the dictionary

print(mainMember.keys())
print(mainMember.values())  
