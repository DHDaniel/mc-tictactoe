
import copy
import random

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
        self.identifier = self.board.get_identifier(self.player)

        self.scores = [[0 for col in self.board.horizontals[0]] for row in self.board.horizontals]

    def update_board(self, new_board):
        """
        Takes in a TTTBoard and updates the internal one to the new one
        """
        self.board = copy.deepcopy(new_board)
        self.original_board = copy.deepcopy(new_board)
        # re-setting scores
        self.scores = [[0 for col in self.board.horizontals[0]] for row in self.board.horizontals]

    def mc_trial(self):
        """
        Performs a simulation of the game.
        Plays a whole game, making random moves on the board, starting with his own move. Modifies
        the internal board, doesn't return anything
        """
        turn = True
        while self.board.is_full() == False and self.board.is_won() == False:
            empty_coord = self.board.random_empty_square()
            self.board.play_square(empty_coord[0], empty_coord[1], self.player if turn else self.opponent)
            turn = not turn

    def mc_update_scores(self):
        """
        Updates move scores based on the current state of the board
        """
        if self.board.is_won() == False:
            # do nothing if game was a draw
            return
        else:
            winning_player = self.board.is_won()
            machine_won = True if winning_player == self.identifier else False

            # if the machine won, then each square that the machine played in recieves a positive score
            # and each square it did not play in recieves a negative score. Empty squares recieve 0.
            # if it didn't win, then the opposite happens.
            if machine_won:
                for horizontal in self.board.horizontals:
                    for coord in horizontals:
                        identifier = self.board.get_square(coord[0], coord[1])
                        if identifier == self.identifier:
                            self.scores[coord[1], coord[0]] += 1
                        elif identifier == 0:
                            return
                        else:
                            self.scores[coord[1], coord[0]] -= 1
            else:
                for horizontal in self.board.horizontals:
                    for coord in horizontals:
                        identifier = self.board.get_square(coord[0], coord[1])
                        if identifier == self.identifier:
                            self.scores[coord[1], coord[0]] -= 1
                        elif identifier == 0:
                            return
                        else:
                            self.scores[coord[1], coord[0]] += 1

    def get_best_move(self):
        """
        Returns a random best move using the scores for each one.
        """
        current_best = None
        best_coords = []

        # getting best score
        for row in scores:
            for score in row:
                if current_best is None:
                    current_best = score
                else:
                    if score > current_best:
                        current_best = score

        # getting all coordinates that have the 'best score'
        for y in xrange(scores):
            for x in xrange(scores[0]):
                score = scores[y][x]
                if score == current_best:
                    best_coords.append([x, y])

        # returning random best move
        return random.choice(best_coords)
