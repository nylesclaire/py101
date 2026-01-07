# expected inputs: bill amount and tip rate
# expected outputs: tip amount and the total bill

# test case 1: 35.73 and 20%, tip 7.15 and total 42.88

# The format specification {:.2f} ensures that the output is formatted to two decimal places. 

bill = float(input("What is the bill amount? "))
tip_rate = float(input("What is the tip percentage? "))

tip = round(bill * (tip_rate / 100), 2)
total = bill + tip

print(f"The tip is ${tip}")
print(f"The total is ${total:.2f}")