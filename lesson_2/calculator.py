import json

with open('calculator_messages.json', 'r') as file:
    mess = json.load(file)

language = "en"

def prompt(key, optional=None):
    message = mess[language][key]
    if optional is not None:
        print(f'==> {message}',optional)
    else:
        print(f'==> {message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

# Welcome user to the program
prompt("hi")

while True:
    # Ask user for the first number & validate it
    prompt("first")
    number1 = input()

    while invalid_number(number1):
        prompt("inval")
        number1 = input()

    # Ask user for the second number & validate it
    prompt("second")
    number2 = input()

    while invalid_number(number2):
        prompt("inval")
        number2 = input()

    # Ask user what operation they want to perform & validate their input
    prompt("oper")
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt("oper_inval")
        operation = input()

    # Perform the operation
    match operation:
        case '1':     # '1' represents addition
            output = float(number1) + float(number2)
        case '2':   # '2' represents subtraction
            output = float(number1) - float(number2)
        case '3':   # '3' represents multiplication
            output = float(number1) * float(number2)
        case '4':   # '4' represents division
            try:
                output = float(number1) / float(number2)
            except ZeroDivisionError:
                prompt("divide_by_zero")
                continue

    # Print the result to the terminal.
    prompt("result", output)

    # Ask the user if they'd like to continue.
    prompt("another")
    another = input()

    if another in ['Y', 'y']:
        continue
    prompt("goodbye")
    break