# Mortage / Car Loan Calculator

def prompt(message):
    print(f'==> {message}')

def get_valid_principal():
    prompt('What is the loan amount?')
    while True:
        principal = input()
        try: 
            principal = float(principal)
            break
        except ValueError:
            prompt("That doesn't seem to be a valid number-- try again.")
            continue
    return principal

        
# Welcome message
prompt('Welcome to the Mortgage or Car Loan calculator.')

# Get loan amount (principal) from the user & validate the input
get_valid_principal()

# Get the annual percentage rate (APR) as an integer (5% --> input: '5'), validate
# Calculate the monthly interest rate 

# Get the duration of the loan (in either months or years)
# Convert the duration of the loan to months, if need be


# Perform the calculation
# monthly_payment = principal * (mon_int_rate / (1 - (1 + mon_int_rate) ** (-loan_duration)))

# Print the monthly payment amount in dollars & cents