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
