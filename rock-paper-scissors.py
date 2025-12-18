import random
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def get_player_choice():
    choice = ''
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input(
            Fore.GREEN + "Choose Rock, Paper, or Scissors: " + Style.RESET_ALL
        ).lower()
    return choice

def get_ai_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def decide_winner(player, ai):
    if player == ai:
        return "draw"
    elif (
        (player == 'rock' and ai == 'scissors') or
        (player == 'paper' and ai == 'rock') or
        (player == 'scissors' and ai == 'paper')
    ):
        return "player"
    else:
        return "ai"

def play_game():
    print(Fore.MAGENTA + "✊✋✌ Welcome to Rock Paper Scissors ✊✋✌")
    name = input(Fore.CYAN + "Enter your name: " + Style.RESET_ALL)

    player_score = 0
    ai_score = 0

    while True:
        player_choice = get_player_choice()
        ai_choice = get_ai_choice()

        print(Fore.YELLOW + f"\n{name} chose: {player_choice}")
        print(Fore.RED + f"AI chose: {ai_choice}")

        result = decide_winner(player_choice, ai_choice)

        if result == "player":
            print(Fore.GREEN + "🎉 You win this round!")
            player_score += 1
        elif result == "ai":
            print(Fore.RED + "💀 AI wins this round!")
            ai_score += 1
        else:
            print(Fore.BLUE + "😐 It's a draw!")

        print(Fore.CYAN + f"\nScore → {name}: {player_score} | AI: {ai_score}")

        again = input(
            Fore.MAGENTA + "\nPlay again? (y/n): " + Style.RESET_ALL
        ).lower()
        if again not in ['y', 'yes']:
            print(Fore.GREEN + "\nThanks for playing! 👋")
            break

if __name__ == "__main__":
    play_game()
