# Write a function that takes one integer argument and returns True 
# when the number's absolute value is odd, False otherwise.

# expected input: an integer
# expected output: True or False

# test cases: 5, 4, 1, 0, -5, -6, 233, 234

def is_it_odd(number):
    return abs(number) % 2 != 0

print("5: ",is_it_odd(5))
print("4: ",is_it_odd(4))
print("1: ",is_it_odd(1))
print("0: ",is_it_odd(0))
print("-5: ",is_it_odd(-5))
print("-6: ",is_it_odd(-6))
print("233: ",is_it_odd(233))
print("234: ",is_it_odd(234))