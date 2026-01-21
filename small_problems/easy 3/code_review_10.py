def yes_no_response(question):
    while True:
        answer = input(f"{question}")
        answer = answer.lower().strip()

        if answer in ["y", "yes"]:
            print("Here we go again!")
            return
        elif answer in ["n", "no"]:
            print("Okay. See you later.")
            return
        else: 
            print("You goofed! That is not a valid answer.")

yes_no_response("Do you want to continue? (y/n)")
yes_no_response("Are you absolutely sure? (yes/no)")
print("All done.")