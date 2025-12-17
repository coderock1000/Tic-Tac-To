import random
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

# ---------- GAME LOGIC ----------
def check_win(board, symbol):
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == symbol:
            return True
    return False

def check_full(board):
    return all(not spot.isdigit() for spot in board)

# ---------- DISPLAY ----------
def display_board(board):
    print()
    print(Fore.CYAN + f" {board[0]} | {board[1]} | {board[2]}")
    print(Fore.CYAN + "---|---|---")
    print(Fore.CYAN + f" {board[3]} | {board[4]} | {board[5]}")
    print(Fore.CYAN + "---|---|---")
    print(Fore.CYAN + f" {board[6]} | {board[7]} | {board[8]}")
    print()

# ---------- PLAYER SETUP ----------
def player_choice():
    choice = ''
    while choice not in ['X', 'O']:
        choice = input(Fore.GREEN + "Choose X or O: " + Style.RESET_ALL).upper()
    if choice == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# ---------- MOVES ----------
def player_move(board, symbol):
    position = ''
    while position not in [str(i) for i in range(1,10)] or not board[int(position)-1].isdigit():
        position = input(Fore.YELLOW + "Choose a position (1-9): " + Style.RESET_ALL)
    board[int(position)-1] = symbol

def ai_move(board, symbol):
    available = [i for i in range(9) if board[i].isdigit()]
    move = random.choice(available)
    board[move] = symbol
    print(Fore.RED + f"AI chose position {move + 1}")

# ---------- MAIN GAME ----------
def tic_tac_toe():
    print(Fore.MAGENTA + "🎮 Welcome to Tic-Tac-Toe 🎮")
    player_name = input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL)

    while True:
        board = ['1','2','3','4','5','6','7','8','9']
        player_symbol, ai_symbol = player_choice()
        turn = 'Player'
        game_on = True

        while game_on:
            display_board(board)

            if turn == 'Player':
                player_move(board, player_symbol)
                if check_win(board, player_symbol):
                    display_board(board)
                    print(Fore.GREEN + f"🎉 Congratulations {player_name}, you win!")
                    game_on = False
                elif check_full(board):
                    display_board(board)
                    print(Fore.YELLOW + "😐 It's a draw!")
                    game_on = False
                else:
                    turn = 'AI'
            else:
                ai_move(board, ai_symbol)
                if check_win(board, ai_symbol):
                    display_board(board)
                    print(Fore.RED + "💀 AI wins! Better luck next time.")
                    game_on = False
                elif check_full(board):
                    display_board(board)
                    print(Fore.YELLOW + "😐 It's a draw!")
                    game_on = False
                else:
                    turn = 'Player'

        again = input(Fore.CYAN + "Play again? (y/n): " + Style.RESET_ALL).lower()
        if again not in ['y', 'yes']:
            print(Fore.MAGENTA + "Thanks for playing! 👋")
            break

# ---------- RUN ----------
if __name__ == "__main__":
    tic_tac_toe()
