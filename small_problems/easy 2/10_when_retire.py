import datetime

age = int(input("What is your age? "))
r_age = int(input("At what age do you plan to retire? "))

now_year = datetime.datetime.now().year
years_to_go = r_age - age

print(
    f"It's {now_year}. You will retire in {now_year + years_to_go}.\n"
    f"You have only {years_to_go} years of work to go!"
)