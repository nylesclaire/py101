def multiply(factor1, factor2):
    return factor1 * factor2

def square(number):
    return multiply(number, number)

print(square(5) == 25)   # True
print(square(-8) == 64)  # True