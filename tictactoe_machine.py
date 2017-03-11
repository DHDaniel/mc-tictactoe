


"""
This program simulates a game between two machine players using the Monte Carlo method.
Theoretically, it should always end in a draw. However, if you play around with the trials
argument, you might see one of them win and one of them lose.
"""

import sys

from TTTBoard import TTTBoard
from MonteCarloPlayer import MonteCarloPlayer

board = TTTBoard(3, "x", "o")
mc_player_1 = MonteCarloPlayer(board, 1, int(sys.argv[1]))
mc_player_2 = MonteCarloPlayer(board, 2, int(sys.argv[2]))

# player 1 starts the game
turn_player_1 = True
while board.is_full() == False:

    if turn_player_1:

        print "Turn:", board.player_1, "\n"

        move = mc_player_1.move()
        board.play_square(move[0], move[1], 1)

    else:

        print "Turn:", board.player_2, "\n"

        move = mc_player_2.move()
        board.play_square(move[0], move[1], 2)

    mc_player_1.update_board(board)
    mc_player_2.update_board(board)

    if board.is_won():
        print board
        print
        print "WINNER:", board.is_won(), "\n"
        break

    print board

    turn_player_1 = not turn_player_1

if board.is_won() == False:
    print "\n WE HAVE A TIE! \n"
