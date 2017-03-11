
"""
This program lets you play, via the console, against the machine. Good luck.
The higher you make the Monte Carlo trials, the less likely you are to win.
"""

import sys

from TTTBoard import TTTBoard
from MonteCarloPlayer import MonteCarloPlayer

player_number = int(raw_input("What player do you wish to be? (1 or 2 -- 1 goes first): "))
machine_number = 2 if player_number == 1 else 1


# printing rules
print "When it is your turn, you will be prompted to enter two numbers, separated by spaces. They are the x and y coordinates that you wish to play in, the top-left square being '0 0' and the bottom-right square being '3 3'. The x coordinate goes from left-to-right, the y coordinate goes from top-to-bottom.\n\n"

board = TTTBoard(3, "X", "O")
mc_player = MonteCarloPlayer(board, machine_number, int(sys.argv[1]))

player_turn = True if player_number == 1 else False

while board.is_full() == False:

    print
    print board
    print

    print "You are", "X" if player_number == 1 else "O"
    print "Machine is", "O" if player_number == 1 else "X"
    print


    if player_turn:

        # checking if move is valid
        while True:
            raw_move = raw_input("Enter your move: ")
            raw_move = raw_move.split()
            move = (int(raw_move[0]), int(raw_move[1]))

            if board.is_within(move[0], move[1]) and board.get_square(move[0], move[1]) == 0:
                break
            else:
                print "Please enter a valid move."
                continue

        board.play_square(move[0], move[1], player_number)

    else:
        move = mc_player.move()
        board.play_square(move[0], move[1], machine_number)

        print "Machine plays", move


    mc_player.update_board(board)

    if board.is_won():
        print board
        print
        print "WINNER:", board.is_won(), "\n"
        break

    player_turn = not player_turn



if board.is_won() == False:
    print "\n WE HAVE A TIE! \n"
