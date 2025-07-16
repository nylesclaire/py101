import json

with open('calculator_messages.json', 'r') as file:
    mess = json.load(file)

#print(mess)

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

# Welcome user to the program
prompt(mess["hi"])

while True:
    # Ask user for the first number & validate it
    prompt(mess["first"])
    number1 = input()

    while invalid_number(number1):
        prompt(mess["inval"])
        number1 = input()

    # Ask user for the second number & validate it
    prompt(mess["second"])
    number2 = input()

    while invalid_number(number2):
        prompt(mess["inval"])
        number2 = input()

    # Ask user what operation they want to perform & validate their input
    prompt(mess["oper"])
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(mess["oper_inval"])
        operation = input()

    # Perform the operation
    match operation:
        case '1':     # '1' represents addition
            output = int(number1) + int(number2)
        case '2':   # '2' represents subtraction
            output = int(number1) - int(number2)
        case '3':   # '3' represents multiplication
            output = int(number1) * int(number2)
        case '4':   # '4' represents division
            output = int(number1) / int(number2)

    # Print the result to the terminal.
    prompt((mess["result"] + str(output)))

    # Ask the user if they'd like to continue.
    prompt(mess["another"])
    another = input()

    if another in ['Y', 'y']:
        continue
    prompt(mess["goodbye"])
    break