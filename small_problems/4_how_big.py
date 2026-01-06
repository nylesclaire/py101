# expected input: length and width in meters - natural numbers or positive floats
# expected output: area in square meters, area in square feet

# test case1: 4 meters by 5 meters, 20 sq meters or 215.78 sq ft
# test case2: 0 meters by 5 meters, should be 0 and 0
# test case3: -5 meters by -9 meters, should be 45 sq meters or 484.376
# test case4: 1 meter by 30 meters, 30 sq meters or 322.917 sq ft
# test case5: 4.3 meters by 4 meters, 17.2 sq meters or 185.1393 sq ft

def prompt(message):
    print(f'==> {message}')

prompt("Welcome to the room area calculator.")

prompt("Please input the length in meters.")
length = float(input())
prompt("Please input the width in meters.")
width = float(input())

square_meters_area = length * width
square_feet_area = square_meters_area * 10.7639

prompt(
    f"The area is {square_meters_area} square meters, "
    f"or {square_feet_area} square feet."
)