# Mortage / Car Loan Calculator

def prompt(message):
    print(f'==> {message}')

def get_valid_principal():
    prompt('What is the loan amount?')
    while True:
        user_principal = input()
        try:
            user_principal = float(user_principal)
            break
        except ValueError:
            prompt("That doesn't seem to be a valid number-- try again.")
            continue
    return user_principal

def get_valid_apr():
    prompt('''What is the Annual Percentage Rate (APR)?
           Please provide the percentage itself; for example, if your APR is 5.5%,
           please type in 5.5.''')
    while True:
        user_apr = input()
        try:
            user_apr = float(user_apr)
            if 0 <= user_apr < 100:
                break
            prompt("That doesn't seem to be a valid number-- try again.")
            continue
        except ValueError:
            prompt("That doesn't seem to be a valid number-- try again.")
            continue
    return user_apr


def get_valid_duration():
    prompt("""What is the duration of the loan? Enter the number of months,
           or press 'y' to enter the duration in years.""")
    while True:
        user_loan_dur = input()
        if user_loan_dur in ['y','Y','years']:
            prompt("What is the duration in years?")
            while True:
                years_dur = input()
                try:
                    years_dur = float(years_dur)
                    user_loan_dur = years_dur * 12
                    break
                except ValueError:
                    prompt("That doesn't seem to be \
                           a valid number-- try again.")
                    continue
        try:
            user_loan_dur = int(user_loan_dur)
            break
        except ValueError:
            prompt("That doesn't seem to be a valid number-- try again.")
            continue
    return user_loan_dur


# Welcome message
prompt('Welcome to the Mortgage or Car Loan calculator.')

while True:
    # Get loan amount (principal) from the user & validate the input
    principal = get_valid_principal()

    # Get the annual percentage rate (APR), validate
    apr = get_valid_apr()
    # Calculate the monthly interest rate
    mon_int_rate = apr / 1200

    # Get the duration of the loan (in either months or years)
    # Convert the duration of the loan to months, if need be
    loan_duration = get_valid_duration()

    # Perform the calculation
    if apr == 0:
        monthly_payment = principal / loan_duration
    else:
        monthly_payment = principal * (mon_int_rate /
                                (1 - (1 + mon_int_rate) ** (-loan_duration)))

    # Print the monthly payment amount in dollars & cents
    prompt(f"Your monthly payment will be: ${monthly_payment:.2f}.")

    # Ask user if they'd like to go again
    prompt("""Would you like to perform another calculation?
            Press 'Y' to continue.""")
    again = input()
    if again in ['y','Y']:
        prompt("------------------------------------")
        continue
    prompt("Thanks for using the calculator. Bye!")
    break