print("hello world")

# this is a comment
"""
multiline comment
which i can write here 
here
and here
"""

# variables
x = 12
y = 15
z = "hello"
print(z)

# strings
a = "hello mate "
b = "Aye sir"
print(a[0])

# looping through strings
for i in a:
    print(i)

# slicing string
print(a[1:5])

# string methods
print(a.upper())
print(a.lower())
print(a + b)

# list

mylist = ["siddhant", "sam", "robert"]
print(len(mylist))
mylist[1] = "tony"

mylist.append("stark")
mylist.insert(2, "zebra")
print(mylist)

# tuples

mytuple = ("sid", "dan", "mozart")

# set

myset = {"hi", "hello", "bye"}

# dictionary

mydictionary = {
    "name": "siddhant",
    "age": 12,
    "number": 7878777777
}
