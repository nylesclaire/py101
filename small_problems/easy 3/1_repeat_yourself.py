# expected input: a string and a positive integer
# expected output: several strings

def repeat(string, number):
    for element in range(1, number+1):
        print(string)

repeat('Hello', 3)