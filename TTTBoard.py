


import unittest
import random

####################
#   GENERAL UTILITY FUNCTIONS
####################

def are_all_the_same(values):
    """
    Takes in a list and returns whether all values are the same, and not 0 (empty)
    """
    if 0 in values:
        return False

    first_value = values[0]
    for value in values:
        if value != first_value:
            return False

    return True


####################
#   MAIN CLASS
####################

class TTTBoard:

    def __init__(self, dimension, player_1_identifier, player_2_identifier):
        """
        Initialises the board, taking in the dimensions for it and the desired identifier
        for player 1 and player 2. Identifiers could be numbers or letters.
        """
        # setting basic variables and identifiers
        self.board = [[0 for i in xrange(dimension)] for j in xrange(dimension)]
        self.player_1 = player_1_identifier
        self.player_2 = player_2_identifier

        # making lists of coordinates for specific directions, to check for wins later
        self.verticals = [[ [x_coord, y_coord] for y_coord in xrange(dimension)] for x_coord in xrange(dimension)]
        self.horizontals = [[ [x_coord, y_coord] for x_coord in xrange(dimension)] for y_coord in xrange(dimension)]
        self.diagonals = []

        # vector diagonal directions running towards the right and towards the left
        diag_offset_right = (1, 1)
        diag_offset_left = (-1, 1)

        top_left = (0, 0)
        top_right = (dimension - 1, 0)

        current_left = [top_left[0], top_left[1]]
        current_right = [top_right[0], top_right[1]]

        # creating first diagonal running from top left to bottom right
        right_diag = []
        while self.is_within(current_left[0], current_left[1]):
            right_diag.append(current_left[:]) # copying the list to avoid problems with references
            current_left[0] += diag_offset_right[0]
            current_left[1] += diag_offset_right[1]

        # creating second diagonal running from top right to bottom left
        left_diag = []
        while self.is_within(current_right[0], current_right[1]):
            left_diag.append(current_right[:]) # copying the list to avoid problems with references
            current_right[0] += diag_offset_left[0]
            current_right[1] += diag_offset_left[1]

        # adding them to the diagonals list
        self.diagonals.append(right_diag)
        self.diagonals.append(left_diag)


        if self.player_1 == self.player_2:
            raise ValueError("Identifiers for player 1 and player 2 cannot be the same.")

        if self.player_1 == 0 or self.player_2 == 0:
            raise ValueError("Identifiers cannot be 0.")


    def __str__(self):
        return_string = "Current board status:\n\n\n"

        for row in self.board:
            row_str = str(row) + "\n\n"
            return_string += row_str

        return_string += "Player 1: " + str(self.player_1) + "\n"
        return_string += "Player 2: " + str(self.player_2) + "\n"
        return return_string

    def get_square(self, x_coord, y_coord):
        """
        Returns the value of a specific square in the board
        """
        if self.is_within(x_coord, y_coord):
            return self.board[y_coord][x_coord]
        else:
            raise IndexError("Coordinates (" + str(x_coord) + ", " + str(y_coord) + ") are out of range.")

    def play_square(self, x_coord, y_coord, player):
        """
        Inserts value into a certain square, given by the coordinates.
        "Player" is a number representing either player 1 or player 2
        """
        if player == 1:
            player = self.player_1
        elif player == 2:
            player = self.player_2
        else:
            raise ValueError("Player must be either '1' or '2'.")

        if self.is_within(x_coord, y_coord) == False:
            raise IndexError("Coordinates (" + str(x_coord) + ", " + str(y_coord) + ") are out of range.")

        if self.get_square(x_coord, y_coord) != 0:
            raise ValueError("The square you are trying to play in is already taken.")

        # if no exceptions are raised, play
        self.board[y_coord][x_coord] = player

    def is_won(self):
        """
        Returns whether board has a winner, and if it does, returns the "symbol" that has won
        """
        for horizontal in self.horizontals:
            horizontal_values = []
            for coord in horizontal:
                horizontal_values.append(self.get_square(coord[0], coord[1]))
            if are_all_the_same(horizontal_values):
                return horizontal_values[0]

        for vertical in self.verticals:
            vertical_values = []
            for coord in vertical:
                vertical_values.append(self.get_square(coord[0], coord[1]))
            if are_all_the_same(vertical_values):
                return vertical_values[0]

        for diagonal in self.diagonals:
            diagonal_values = []
            for coord in diagonal:
                diagonal_values.append(self.get_square(coord[0], coord[1]))
            if are_all_the_same(diagonal_values):
                return diagonal_values[0]

        # there is no winner yet
        return False

    def is_full(self):
        """
        Returns whether the board has any empty spaces left
        """
        for horizontal in self.horizontals:
            for coord in horizontal:
                if self.get_square(coord[0], coord[1]) == 0:
                    return False
        return True

    def random_empty_square(self):
        """
        Returns a random empty square (coordinates) from the board. This utility is most useful for
        the Monte Carlo simulations. Returns None if board is already full.
        """
        if self.is_full():
            return None

        empty_square_coords = []
        for horizontal in self.horizontals:
            for coord in horizontal:
                if self.get_square(coord[0], coord[1]) == 0:
                    empty_square_coords.append(coord[:]) # appending copy of coordinate

        return random.choice(empty_square_coords)

    def is_within(self, x_coord, y_coord):
        """
        Returns whether coordinates are inside the board. Doesn't accept negative coordinates
        """
        if x_coord < 0 or y_coord < 0:
            return False

        try:
            val = self.board[y_coord][x_coord]
            # if there are no errors, then it is a valid coordinate
            return True
        except:
            return False


#####################
# TESTING CLASS
#####################

class TTTBoardTester(unittest.TestCase):

    def test_init(self):
        board = TTTBoard(4, "x", "o")

        # checking basic lengths
        self.assertEqual(len(board.horizontals), 4)
        self.assertEqual(len(board.diagonals), 2)
        self.assertEqual(len(board.verticals), 4)

        # checking essential diagonal coordinates
        self.assertEqual(board.diagonals[-1][-1], [0, 3])
        self.assertEqual(board.diagonals[-1][0], [3, 0])
        self.assertEqual(board.diagonals[0][0], [0, 0])
        self.assertEqual(board.diagonals[0][-1], [3, 3])

        # checking essential vertical coordinates
        self.assertEqual(board.verticals[0][0], [0, 0])
        self.assertEqual(board.verticals[0][1], [0, 1])
        self.assertEqual(board.verticals[0][-1], [0, 3])
        self.assertEqual(board.verticals[-1][0], [3, 0])
        self.assertEqual(board.verticals[-1][-1], [3, 3])

        # checking identifiers cannot be the same
        self.assertRaises(ValueError, TTTBoard, 4, "x", "x")
        self.assertRaises(ValueError, TTTBoard, 4, 1, 1)

    def test_play(self):
        board = TTTBoard(3, "x", "o")

        self.assertEqual(board.board[0][0], 0)

        board.play_square(0, 0, 1)
        self.assertEqual(board.board[0][0], "x")

        board.play_square(0, 1, 2)
        self.assertEqual(board.board[1][0], "o")

        # checking playing outside box raises error
        self.assertRaises(IndexError, board.play_square, 3, 3, 1)
        self.assertRaises(IndexError, board.play_square, 2, 3, 1)
        self.assertRaises(IndexError, board.play_square, 3, 2, 1)
        self.assertRaises(IndexError, board.play_square, -1, 2, 1)

        # checking playing an invalid player
        self.assertRaises(ValueError, board.play_square, 2, 2, 3)

        # checking playing an already played coordinate
        # first square has already been played in
        self.assertRaises(ValueError, board.play_square, 0, 0, 1)

    def test_get_square(self):
        board = TTTBoard(3, "x", "o")

        self.assertEqual(board.get_square(1, 2), 0)

        # not using the 'play' method because we are not testing it here
        board.board[2][1] = "x"
        self.assertEqual(board.get_square(1, 2), "x")

        self.assertRaises(IndexError, board.get_square, 3, 3)
        self.assertRaises(IndexError, board.get_square, -1, -1)

    def test_is_won(self):
        board = TTTBoard(3, "x", "o")
        self.assertFalse(board.is_won())

        # winning vertical
        board.play_square(1, 0, 1)
        board.play_square(1, 1, 1)
        board.play_square(1, 2, 1)
        self.assertEqual(board.is_won(), "x")

        board = TTTBoard(3, "x", "o")
        # winning horizontal
        board.play_square(0, 1, 1)
        board.play_square(1, 1, 1)
        board.play_square(2, 1, 1)
        self.assertEqual(board.is_won(), "x")

        board = TTTBoard(3, "x", "o")
        # winning diagonal
        board.play_square(2, 0, 1)
        board.play_square(1, 1, 1)
        board.play_square(0, 2, 1)
        self.assertEqual(board.is_won(), "x")

        board = TTTBoard(3, "x", "o")
        # filling row but no winner
        board.play_square(0, 0, 1)
        board.play_square(1, 0, 2)
        board.play_square(2, 0, 1)
        self.assertFalse(board.is_won())

    def test_is_full(self):
        board = TTTBoard(2, "x", "o")

        board.play_square(0, 0, 1)
        board.play_square(0, 1, 1)
        board.play_square(1, 0, 1)

        self.assertFalse(board.is_full())

        board.play_square(1, 1, 1)
        self.assertTrue(board.is_full())

    def test_random_empty_square(self):
        board = TTTBoard(2, "x", "o")

        board.play_square(0, 0, 1)
        board.play_square(0, 1, 1)

        self.assertTrue(board.random_empty_square() in [[1, 0], [1, 1]])

        board.play_square(1, 0, 1)
        self.assertEqual(board.random_empty_square(), [1, 1])

        board.play_square(1, 1, 1)
        self.assertEqual(board.random_empty_square(), None)



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TTTBoardTester)
    unittest.TextTestRunner(verbosity=2).run(suite)
