import random
print("Welcome to the PyPassword Generator!")

# letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Numbers (as strings)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Symbols/Punctuation
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

first_question = int(input("How many letters would you like in your password?\n"))
sec_question = int(input("How many symbols would you like?\n"))
third_question = int(input("How many numbers would you like?\n"))

res = []
resStr = ""

for i in range(first_question):
    newRes = random.choice(letters)
    res.append(newRes)
    resStr += newRes

for i in range(sec_question):
    newRes = random.choice(symbols)
    res.append(newRes)
    resStr += newRes

for i in range(third_question):
    newRes = random.choice(numbers)
    res.append(newRes)
    resStr += newRes

print(res)

'''Hard version of random password generator'''
hard = ""
''' My solution'''
# for i in range(len(resStr)):
#     hard += random.choice(resStr)

# or
'''Angela Yu solution'''
random.shuffle(res)
for i in res:
    hard += i

print(resStr)
print(hard)