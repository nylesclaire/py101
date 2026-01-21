def crunch1(string):
    new_string = ""
    indx = 0

    while indx < len(string):
        if indx == len(string) - 1 or string[indx] != string[indx + 1]:
            new_string += string[indx]
        indx += 1
    return new_string

# for further exploration
# can I find a solution using a for loop
# looping either over indices or characters

def crunch(string):
    new_string = ""
    for index in range(len(string)):
        if index == len(string) - 1 or string[index] != string[index + 1]:
            new_string += string[index]
    return new_string


# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')