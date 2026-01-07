# expected input: positive integer, and s or p for sum or product
# expected output: either the sum or the product of 
# all numbers between 1 and the integer, inclusive.

# test case 1: 5, sum is 15, product is 120
# test case 2: 6, sum is 20, product is 720
# test case 3: -4, should deliver error message
# test case 4: "Sally", should deliver error message
# test case 5: 5, then "a", should deliver error message
# test case 6: 5, then "S", to test capital letter

def invalid_number(num):
    try:
        int(num)
    except ValueError:
        return True
    if int(num) < 0:
        return True
    return False

def invalid_operation(answer):
    if answer in ['s', 'S', 'p', 'P']:
        return False
    return True

number = (input("Please enter an integer greater than 0. "))

while invalid_number(number):
    number = input("That's an invalid number- try again. ")

number = int(number)

operation = input("Enter 's' to compute the sum, or 'p' to compute the product. ")

while invalid_operation(operation):
    operation = input("That's an invalid answer- try again.")

if operation in ['s', 'S']:
    summation = 0
    for element in range(1, number + 1):
        summation = summation + element
    print(f"The sum of the integers between 1 and {number} is {summation}.")
elif operation in ['p', 'P']:
    product = 1
    for element in range(1, number + 1):
        product = product * element
    print(f"The product of the integers between 1 and {number} is {product}.")