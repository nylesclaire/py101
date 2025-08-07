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
    else:
        return False
    
def computer_won(player_choice, computer_choice):
    if player_choice in WINNER_COMBOS[computer_choice]:
        return True
    else:
        return False

def display_winner(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")
    if player_won(player, computer):
        prompt("You won!")
    elif player == computer:
        prompt("It's a tie.")
    else:
        prompt("The computer won!")

#Begin main program
player_total_wins = 0
computer_total_wins = 0
current_game = 1

while True:
    prompt("Let's play Best of Five!")
    while player_total_wins < 3 and computer_total_wins < 3:
        prompt(f"Game {current_game}:")
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

        current_game += 1

        if player_won(choice, computer_chooses):
            player_total_wins += 1
        elif computer_won(choice, computer_chooses):
            computer_total_wins += 1

    if player_total_wins <= 3:
        prompt("You're the grand winner!")
    else:
        prompt("The computer is the grand winner!")

    while True:
        prompt("Do you want to play again (y/n)?")
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        else:
            prompt("That's not a valid choice")

    if answer[0] == 'n':
        break
    else:
        prompt("Thanks for playing. Bye!")