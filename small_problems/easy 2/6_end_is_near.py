def penultimate(string):
    string_list = string.split()
    return string_list[-2]

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")



#further exploration
# test case 1: "Hello" (string with one word) >> "Hello"
# test case 2: "" (string with no words) >> ""
# test case 3: "Hello it's me." >> "it's"
# test case 4: "I want to see the city." >> "to see"
# test case 5: "Cresto, it's okay, baby." >> "it's okay"

def middle_words(words):
    if words == "":
        return None
    words = words.replace(",", "")
    words_list = words.split()
    half = int(len(words_list) // 2)
    if len(words_list) % 2 == 0:
        return (f"{words_list[half-1]} {words_list[half]}")
    else:
        return (f"{words_list[half]}")

print(middle_words("Hello"))
print(middle_words(""))
print(middle_words("Hello it's me."))
print(middle_words("I want to see the city."))
print(middle_words("Cresto, it's okay, baby."))
