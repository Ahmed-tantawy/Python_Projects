#------------------------------
# --- String Indexing & Slicing ---
# [1] All Data is python is Object
# [2] Object contain Elements
# [3] Every elment has an Index
# [4] Python Zero Based Indecing (Undex start from Zeero)
# [5] Use [] to access elements in a string
# [6] Use : to Slice a string
# [7] Enable Accesssing parts of a strings, Tuples and Lists
#------------------------------

myStringone = "Hello, World!"
myStringtwo = 'Python Programming'
myStringthree = "This is a 'test' string"


print(myStringone)  # Output: Hello, World!irstName = "Ahmed"
print(myStringtwo)  # Output: Python Programming
print(myStringthree)  # Output: This is a multi-line string

myStringfour = """This is a
multi-line string
using triple quotes."""
print(myStringfour) # Output: This is a multi-line string using triple quotes.


# Indexing (Accessiing single Item)

mystr= "I love Python"
print(mystr[0])  # Output: I
print(mystr[7])  # Output: P

print(mystr[-1]) # Output: n (Last Character)
print(mystr[-6]) # Output: P (6th Character from the end)

# Slicing (Accessing a range of characters) [start: end: step]
print(mystr[1:6])  # Output: love (Characters from index 2 to 5)
print(mystr[:6])   # Output: I love (Characters from start

print(mystr[3:5]) # output : ov

print(mystr[0::3]) # output : I o yhn (Every 3rd character from the start)

#-----------------------------------------------
# --- String Method ---
#-----------------------------------------------

print(len(mystr)) # Output: 13 (Length of the string # It counts the string NOT the index)

mystr2 = "hello,             world!"
print(len(mystr2))  # Output: 25 (Length of the string with spaces)

#---------------------------------------
# --- String Methods ------
# stript() - Remove whitespace from the beginning and end
# rstrip() - Remove whitespace from the end
# lstrip() - Remove whitespace from the beginning
#---------------------------------------

mystr3 = "#####Hello, World! @@  "
print(mystr3.strip('#@'))  # Output: Hello, World!

#tile() - Convert the first character of each word to uppercase
mystr5 = "I love 2rd graphics and 3g technology and python"
print(mystr5.title()) # Output: I Love Python

print(mystr5.capitalize()) # Output: I love python (First Character to Uppercase)

#zfill() - Pad a numeric string on the left with zeros to fill a width

d, e, r, o = "1", "10", "111", "1111"

print(d.zfill(4))
print(e.zfill(4))
print(r.zfill(4))
print(o.zfill(4))

#Upper() - Convert a string to uppercase
#Lower() - Convert a string to lowercase

#split() - Split a string into a list of substrings based on a delimiter (default is whitespace)

mystr6 = "I love python and Groovy and PostgreSQL "

mystr7 = "I-love-python-and-Groovy and PostgreSQL "

print(mystr6.split()) 
print(mystr7.split('-'))
#suing the max in the split
print(mystr6.split(' ', 2)) # Output: ['I', 'love',

#using rsplit to split from the right
print(mystr6.rsplit(' ', 3)) # Output: ['I love python and', 'Groovy', 'and', 'PostgreSQL']
l = 'PostgreSQL'
#center()
print(l.center(9))
print(l.center(20, '*'))
print(l.center(15, '#'))

#count() - Count the occurrences of a substring in a string #Case Sensitive
q = "I Love python and Groovy and PostgreSQL and python"
print(q.count('and')) # Output: 3rom the start to index 5)

#swapcase() - Swap the case of each character in the string

print(q.swapcase()) # Output: i LOVE PYTHON AND gROOVY AND pOSTGRESql AND PYTHON

# startswith)() - Check if a string starts with a specified substring #returns Boolean
print(q.startswith('Me')) # Output: True

#srtartswith() - Check if a string ends with a specified substring #returns Boolean

i = "I Love Python"

print(i.startswith('I')) # Output: True
print(i.startswith('P', 7, 13)) # Output: True

#endswith()
print(i.endswith('n')) # Output: True
print(i.endswith('L', 2, 6)) # Output: True

# index()

a = " I love Python"
print(a.index('P')) # Output: 7 (Index of the first occurrence of 'P')

print(a.index('P',0, 10)) # Output: 7 (Index of 'P' between index 0 and 10)
# print(a.index('P'),0,5) # Output: ValueError (Substring not found in the specified range)

print(a.find('p', 0, 5))

# rjust () -  a string to the right within a specified width
# ljust () - l a string to the left within a specified width

print(l.ljust(20, '*'))
print(l.rjust(20, '#'))

# splitlines() - Split a string into a list of lines
m = """Hello, World!
Welcome to Python programming.
Enjoy coding!"""

print(type(m.splitlines()))


m = "Hello, World!\nWelcome to Python programming.\nEnjoy coding!"
print(m.splitlines())

#expandtabs() - Replace tab characters with spaces, using a specified tab size  
n = "Hello,\tWorld!\tWelcome to\tPython."
print(n.expandtabs(4))  # Output: Hello,   World!  Welcome to

one = "I Love Pyhton And 3G"
two = "I Love Pyhton and 3g"
print(one.istitle())
print(two.istitle())

#-----------------------------------------------
# --- Comprehensive String Methods Examples ---
#-----------------------------------------------

example_string = "  Hello, World! Welcome to Python Programming!  "
print(f"Original string: '{example_string}'")
print()

# Length and basic operations
print("=== Length and Basic Operations ===")
print(f"Length: {len(example_string)}")
print(f"First character: '{example_string[0]}'")
print(f"Last character: '{example_string[-1]}'")
print(f"Slice [2:7]: '{example_string[2:7]}'")
print()

# Case operations
print("=== Case Operations ===")
print(f"Upper: {example_string.upper()}")
print(f"Lower: {example_string.lower()}")
print(f"Title: {example_string.title()}")
print(f"Capitalize: {example_string.capitalize()}")
print(f"Swapcase: {example_string.swapcase()}")
print()

# Whitespace operations
print("=== Whitespace Operations ===")
print(f"Strip: '{example_string.strip()}'")
print(f"Lstrip: '{example_string.lstrip()}'")
print(f"Rstrip: '{example_string.rstrip()}'")
print()

# Alignment operations
print("=== Alignment Operations ===")
clean_text = "Python"
print(f"Center (20, '*'): '{clean_text.center(20, '*')}'")
print(f"Ljust (20, '-'): '{clean_text.ljust(20, '-')}'")
print(f"Rjust (20, '#'): '{clean_text.rjust(20, '#')}'")
print(f"Zfill (10): {'123'.zfill(10)}")
print()

# Search and check operations
print("=== Search and Check Operations ===")
search_text = "Python Programming Language"
print(f"Find 'gram': {search_text.find('gram')}")
print(f"Index 'Pro': {search_text.index('Pro')}")
print(f"Count 'a': {search_text.count('a')}")
print(f"Startswith 'Python': {search_text.startswith('Python')}")
print(f"Endswith 'Language': {search_text.endswith('Language')}")
print()

# Split operations
print("=== Split Operations ===")
split_text = "apple,banana,cherry,date"
print(f"Split by comma: {split_text.split(',')}")
print(f"Split by comma (max 2): {split_text.split(',', 2)}")
print(f"Rsplit by comma (max 2): {split_text.rsplit(',', 2)}")
multiline_text = "Line 1\nLine 2\nLine 3"
print(f"Splitlines: {multiline_text.splitlines()}")
print()

# Character type checks
print("=== Character Type Checks ===")
test_strings = ["123", "abc", "ABC", "Hello World", "HELLO", "hello"]
for s in test_strings:
    print(f"'{s}': isdigit={s.isdigit()}, isalpha={s.isalpha()}, isalnum={s.isalnum()}, "
          f"isupper={s.isupper()}, islower={s.islower()}, istitle={s.istitle()}")
print()

# Expandtabs example
print("=== Expandtabs ===")
tab_text = "Name:\tJohn\tAge:\t25"
print(f"Original: {tab_text}")
print(f"Expandtabs(4): {tab_text.expandtabs(4)}")
print(f"Expandtabs(8): {tab_text.expandtabs(8)}")
print()
