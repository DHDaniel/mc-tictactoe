
import copy

class MonteCarloPlayer:

    def __init__(self, TTT_board, player):
        """
        Initialises a machine player which chooses moves based on Monte Carlo simulations.
        TTT_board should be of the class TTTBoard
        """
        try:
            TTT_board.get_square(0, 0)
        except:
            raise ValueError("Board given does not appear to be of the type TTTBoard.")

        self.board = copy.deepcopy(TTT_board)
        # keeping a copy of the original
        self.original_board = copy.deepcopy(self.board)

        # player should be either 1 or 2
        self.player = player
        self.opponent = 2 if self.player == 1 else 1

        self.scores = [[0 for col in self.board.horizontals[0]] for row in self.board.horizontals]

    def update_board(self, new_board):
        """
        Takes in a TTTBoard and updates the internal one to the new one
        """
        self.board = copy.deepcopy(new_board)
        # re-setting scores
        self.scores = [[0 for col in self.board.horizontals[0]] for row in self.board.horizontals]

    def mc_trial(self):
        """
        Plays a whole game, making random moves on the board, starting with his own move. Modifies
        the internal board, doesn't return anything
        """
        turn = True
        while self.board.is_full() == False and self.board.is_won() == False:
            empty_coord = self.board.random_empty_square()
            self.board.play_square(empty_coord[0], empty_coord[1], self.player if turn else self.opponent)
            turn = not turn

    def mc_update_scores(self):
        pass
