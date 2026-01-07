# with further exploration additions

import random

age = random.choice(range(20, 101))
name = input("What is the birthday human's name? ")
if name == "":
    name = "Teddy"

print(f"{name} is {age} years old!")