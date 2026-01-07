
def center_of(words):
    half = int(len(words) // 2)
    if len(words) % 2 == 0:
        return (words[half-1] + words[half])
    else:
        return (words[half])
    
print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True