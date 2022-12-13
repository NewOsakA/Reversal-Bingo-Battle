# Reversal Bingo Battle
**Reversal Bingo Battle (RBB)** is a different version of wellknown Bingo. The objective for this game is to avoid getting a line and get rid of rival tokens, the first one reaching 0 is loss.

This game is actually an academic project which is a part of the 01219114/01219115 Programming 1 course at Kasetsart University. The game is made possible using Python 3 and the builtin module.

## Features
- Can be played in Single-player or offline Multiplayer
- Actions that you can choose while in game.
- All time statistics for all user.
  
## Required Software
- Python >= 3.7 w/ Tk/Tcl installed

## Program Design

`Player` : This class is used for create and store all player name and password in Players.json file.

`Data` : This class is used for store all time player statistics in Players.json file.

`Board` : This class is used for store the latest player's bingo board in form of list.


## Code Structure

`Main.py` : The main file for executing the program, and have all required function in order to run the program.

`Player.py` : The specific file for Player Class, used for create and store player name and password properties.

`Data.py` : The specific file for Data Class, used for saving player statistics.

`Board.py` : The specific file for Board Class, used for store the latest bingo board for all player.

`Players.json` : The file for store players name and password in form of dic.

`Data.py` : The file for store players play time count, win count, lose count and win rate.

`Board.py` : THe file for store the latest bingo board for all player in form of list.



