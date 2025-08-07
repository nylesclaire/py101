import random

CHOICES_DICT = {
    'r':'rock', 
    'p':'paper', 
    's':'scissors', 
    'l':'lizard',
    'v':'spock',
    }

WINNER_COMBOS = {
    'rock': ['scissors', 'lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['spock', 'paper'],
    'spock': ['scissors', 'rock'],
}

def prompt(message):
    print(f"==> {message}")

def player_won(player_choice, computer_choice):
    if computer_choice in WINNER_COMBOS[player_choice]:
        return True

def display_winner(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")
    if player_won(player, computer):
        prompt("You won!")
    elif player == computer:
        prompt("It's a tie.")
    else:
        prompt("The computer won!")

#Begin main program
while True:
    prompt(f"Choose one:")
    for key, value in CHOICES_DICT.items():
        print(f'{key} for {value}') 
    short_choice = input().lower()

    while short_choice not in list(CHOICES_DICT):
        prompt("That's not a valid choice")
        short_choice = input().lower()

    choice = CHOICES_DICT[short_choice]

    computer_chooses = random.choice(list(CHOICES_DICT.values()))

    display_winner(choice, computer_chooses)

    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        else:
            prompt("That's not a valid choice")

    if answer[0] == 'n':
        break