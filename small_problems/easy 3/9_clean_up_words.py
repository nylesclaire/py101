def clean_up(string):
    new_string = ""
    for char in string:
        if ord("A") <= ord(char) <= ord("z"):
            new_string += char
        elif not new_string.endswith(" "):
            new_string += " "
    return new_string

print(clean_up("---what's my +*& line?") == " what s my line ")
# True