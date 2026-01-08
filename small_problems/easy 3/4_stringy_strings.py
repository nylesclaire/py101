def stringy(number):
    if number % 2 == 0:
        return("10" * (number // 2))
    else:
        return("10" * (number // 2) + "1")

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True