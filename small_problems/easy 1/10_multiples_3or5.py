# expected input: positive integer
# expected output: integer 

def multisum(target):
    summation = 0
    for element in range(1, target+1):
        if element % 3 == 0 or element % 5 == 0:
            summation = element + summation
    return summation

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)