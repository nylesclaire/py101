# expected input: two operands (expressions)
# expected output: True or False

def xor(operand1, operand2):
    if bool(operand1) == True and bool(operand2) == False:
        return True
    elif bool(operand1) == False and bool(operand2) == True:
        return True
    else:
        return False
    
print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)