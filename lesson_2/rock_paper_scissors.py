import random

CHOICES_DICT = {
    'r':'rock', 
    'p':'paper', 
    's':'scissors', 
    'l':'lizard',
    'v':'spock',
    }

def prompt(message):
    print(f"==> {message}")

def display_winner(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")

    if ((player == "rock" and computer == "scissors") or
        (player == "rock" and computer == "lizard") or
        (player == "paper" and computer == "rock") or
        (player == "paper" and computer == "spock") or
        (player == "scissors" and computer == "paper") or
        (player == "scissors" and computer == "lizard") or
        (player == "lizard" and computer == "spock") or
        (player == "lizard" and computer == "paper") or
        (player == "spock" and computer == "scissors") or
        (player == "spock" and computer == "rock")):
        prompt("You win!")
    elif ((player == "rock" and computer == "paper") or
        (player == "rock" and computer == "spock") or
        (player == "paper" and computer == "scissors") or
        (player == "paper" and computer == "lizard") or
        (player == "scissors" and computer == "rock") or
        (player == "scissors" and computer == "spock") or
        (player == "lizard" and computer == "scissors") or
        (player == "lizard" and computer == "rock") or
        (player == "spock" and computer == "paper") or
        (player == "spock" and computer == "lizard")):
        prompt("Computer wins!")
    else: 
        prompt("It's a tie!")

while True:
    prompt(f"Choose one:")
    for key, value in CHOICES_DICT.items():
        print(f'{key} for {value}') 
    short_choice = input().lower()

    while short_choice not in list(CHOICES_DICT):
        prompt("That's not a valid choice")
        short_choice = input().lower()

    choice = CHOICES_DICT[short_choice]

    computer_choice = random.choice(list(CHOICES_DICT.values()))

    display_winner(choice, computer_choice)

    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        else:
            prompt("That's not a valid choice")

    if answer[0] == 'n':
        break