# Welcome user to the program
print("Welcome to Calculator!")

# Ask user for the first number
print("What's the first number?")
number1 = int(input())

# Ask user for the second number
print("What's the second number?")
number2 = int(input())

# Ask user what operation they want to perform
print("What operation would you like to perform?\n"
       "1) Add 2) Subtract 3) Multiply 4) Divide")
operation = input()

# Perform the operation
if operation == '1':     # '1' represents addition
    output = number1 + number2
elif operation == '2':   # '2' represents subtraction
    output = number1 - number2
elif operation == '3':   # '3' represents multiplication
    output = number1 * number2
elif operation == '4':   # '4' represents division
    output = number1 / number2

# Print the result to the terminal.
print(f'The result is: {output}')

