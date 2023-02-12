from calculator_ascii_art import logo
import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)
    
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            os.system('clear')
            calculator()

calculator()

# What's the first number?: 12
# +
# -
# *
# /
# Pick an operation: +
# What's the next number?: 20
# 12.0 + 20.0 = 32.0
# Type 'y' to continue calculating with 32.0, or type 'n' to start a new calculation: y
# Pick an operation: *
# What's the next number?: 5
# 32.0 * 5.0 = 160.0
# Type 'y' to continue calculating with 160.0, or type 'n' to start a new calculation: 
