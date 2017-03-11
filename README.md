# Tic Tac Toe: Monte Carlo
This is a console implementation of the classic children's game "Tic Tac Toe" where you can play against the computer. The computer will use Monte Carlo simulations in order to play against you.

## Usage
### Playing against the computer
To play the game, go into the project's directory and run the `tictactoe_player.py` file.
```bash
$ cd /path/to/tictactoe-mc
$ python tictactoe_player.py 1000
```
You will be prompted to choose between being Player 1 and Player 2 ("X" or "O"). A set of instructions will then be printed out, indicating how to enter your desired move.

### Playing machine against machine
You can also pit the computer to play against itself (cruel, I know). To do this, go to the project's directory and run the `tictactoe_machine.py` file
```bash
$ cd /path/to/tictactoe-mc
$ python tictactoe_machine.py 1000 1000
```

### Command line arguments
#### Player version
The command line arguments dictate how many trials the Monte Carlo simulations will use. Basically, the higher the number of trials, the harder it is to beat the computer (although you probably won't manage to beat it unless you use only 1 or 2 trials). A standard "very near perfect" computer player will be around 100 Monte Carlo trials.

`tictactoe_player.py` takes only one argument - the number of trials for the computer to use.

```bash
# a very hard computer player
$ python tictactoe_player.py 1000

# a relatively easier computer player
$ python tictactoe_player.py 200

# an "easy" computer player
$ python tictactoe_player.py 1000
```
#### Computer version
The computer version of the game takes two command line arguments, which represent the number of trials to carry out for player 1 and player 2. If both are high and the same, the computer players will always tie. However, if one is relatively high and the other is relatively low, then the player with highest trials will win occasionally. If the difference is very large, expect the player to almost always win.
```bash
# Player 1 and Player 2 will always tie
$ python tictactoe_machine.py 1000 1000

# Player 1 will sometimes win
$ python tictactoe_machine.py 1000 300

# Player 1 will almost always win
$ python tictactoe_machine.py 1000 10
```

## Contributing
If anyone is skilled at making graphical interfaces, please do get in contact! I would be glad to turn the game into a more user-friendly graphical form.
