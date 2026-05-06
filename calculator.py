def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

'''print("Welcome to ym Calculator")
numQue = float(input("What's the first number?: "))
print("+ \n-\n*\n/")
opeQUe = input("Pick an operation from the above following options: ")
num2Que = float(input("What's the second number?: "))

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
'''

#  Angela yu full solution
print("Welcome to ym Calculator")

def calculator():
    should_continue = True
    numQue = float(input("What's the first number?: "))

    while should_continue:
        for symbol in operations:
            print(symbol)
        opeQUe = input("Pick an operation from the above following options: ")
        num2Que = float(input("What's the second number?: "))
        answer =  operations[opeQUe](numQue, num2Que)
        print(f"{numQue} {opeQUe} {num2Que} = {answer}")

        choice = input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            numQue = answer
        else:
            should_continue = False
            print("\n" * 20)

calculator()