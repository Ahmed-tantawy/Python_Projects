#---------------------------------------
# -----------Concatenation------#
#----------------------------------------

# Basic string concatenation using the + operator
msg = "Hello"
lang = "Python"
print(msg + " " + lang)  # Output: Hello Python

# Concatenating multiple strings
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print("Full name:", full_name)  # Output: Full name: John Doe

# Using f-strings (formatted string literals) - Python 3.6+
age = 25
introduction = f"My name is {full_name} and I am {age} years old"
print(introduction)  # Output: My name is John Doe and I am 25 years old

# Using .format() method
template = "Welcome to {} programming!"
message = template.format(lang)
print(message)  # Output: Welcome to Python programming!

# Using % formatting (older method)
greeting = "Hello %s, you are learning %s" % (first_name, lang)
print(greeting)  # Output: Hello John, you are learning Python

# Concatenating with numbers (need to convert to string)
score = 95
result = "Your score is: " + str(score)
print(result)  # Output: Your score is: 95

# Using join() method for multiple strings
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)  # Output: Python is awesome

# Concatenating strings in a loop
colors = ["red", "green", "blue"]
color_list = ""
for color in colors:
    color_list += color + " "
print("Colors:", color_list.strip())  # Output: Colors: red green blue

# Using += operator for concatenation
countdown = "Countdown: "
for i in range(3, 0, -1):
    countdown += str(i) + "... "
countdown += "Go!"
print(countdown)  # Output: Countdown: 3... 2... 1... Go!

a = "First \t\
    Second \t\
    Third "


b = "A\
    B\
    C\
    D"

print(a + "" +  b)  # Output: First SecondThird AB C  D

