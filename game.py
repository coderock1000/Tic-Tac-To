import colorama
from colorama import Fore, Style

def check_win(board, symbol):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), 
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # 
        (0, 4, 8), (2, 4, 6)             
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == symbol:
            return True
    return False

def check_full(board):
    return all(not spot.isdigit() for spot in board)

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    player_name = input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL)
    while True:
        board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        player_symbol, ai_symbol = player_choice()
        turn = 'Player'
        game_on = True

        while game_on:
            dislay_board(board)
            if turn == 'Player':
                player_move(board, player_symbol)
                if check_win(board, player_symbol):
                    display(board)
                    print(Fore.GREEN + f"Congratulations {player_name}, you win!" + Style.RESET_ALL)
                    game_on = False
                else:
                    if check_full(board):
                        display(board)
                        print(Fore.YELLOW + "It's a draw!" + Style.RESET_ALL)
                        game_on = False
                    else:
                        turn = 'AI'
            else:
                ai_move(board, ai_symbol)
                if check_win(board, ai_symbol):
                    display(board)
                    print(Fore.RED + "AI wins! Better luck next time." + Style.RESET_ALL)
                    game_on = False
                else:
                    if check_full(board):
                        display(board)
                        print(Fore.YELLOW + "It's a draw!" + Style.RESET_ALL)
                        game_on = False
                    else:
                        turn = 'Player'
        player_again = input(Fore.CYAN + "Do you want to play again? (y/n): " + Style.RESET_ALL).lower()
        if player_again == 'yes' or player_again == 'y':
            print(Fore.MAGENTA + "Starting a new game..." + Style.RESET_ALL)
            continue
        else:
            print(Fore.MAGENTA + "Thanks for playing! Goodbye!" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    colorama.init()
    tic_tac_toe()