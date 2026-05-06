def add(a,b):
    return f"{float(a)} + {float(b)} = {float(a) + float(b)}"
def subtract(a,b):
    return f"{float(a)} - {float(b)} = {float(a) - float(b)}"
def multiply(a,b):
    return f"{float(a)} * {float(b)} = {float(a) * float(b)}"
def divide(a,b):
    return f"{float(a)} / {float(b)} = {float(a) / float(b)}"


print("Welcome to ym Calculator")
numQue = int(input("What's the first number?: "))
print("+ \n-\n*\n/")
opeQUe = input("Pick an operation from the above following options: ")
num2Que = int(input("What's the second number?: "))

result = 0

if opeQUe == "+":
    result = add(numQue,num2Que)
    print(result)
elif opeQUe == "-":
    result = subtract(numQue,num2Que)
    print(f"The result is {result}")
elif opeQUe == "*":
    result = multiply(numQue,num2Que)
    print(f"The result is {result}")
elif opeQUe == "/":
    result = divide(numQue,num2Que)
    print(f"The result is {result}")
