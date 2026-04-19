# numerical data types
'''
integer = int()
decimal = float()
complex = complex()
'''

print(type(-100))  #0, 100, 5, -7
print(type(80.75)) #-5.76, 5.00, 5.5
print(type(7 + 2j))

# character data types
'''
(str)
single quoted string ('')
double quoted string ("")
'''
print(type("hi eniola"))
# boolean data types
# True(numbers greater or equals to 1) or False(0, null)
print(type(True))

# so basically we only have 5 basic datatype in python
# int, float, complex, str, bool

var = "eniola"
vars = ""
num = 0
boolean = True
floats = 3.14

for x in var:
    vars += x.capitalize()

print(vars)
print(bool(num))
print(float(10))