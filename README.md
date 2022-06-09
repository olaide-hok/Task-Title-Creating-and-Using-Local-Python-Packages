# Task-Title-Creating-and-Using-Local-Python-Packages

[Rock-Paper-Scissors]
Rock-Paper-Scissors is a simple two-player game where, at a signal, players make figures with their hands, representing a rock, a piece of paper, or a pair of scissors. The winner is determined according to a set of rules. You can find the official rules under the Resources.

 

A brief summary:

If the two players choose the same “character” it’s a tie, and the game repeats
Rock beats Scissors
Paper beats Rock
Scissors beats Paper
You have been tasked to create a simple version of this game with Python. In your version, one player will be controlled by the computer and the other player controlled by you - the user (i.e CPU vs Player). 

Inbuilt Python module random and its choice method is used.

Instructions:

Create a new Python file and call it main.py.
Create a list to store all possible options:
"R" for "rock", 
"P" for "paper", 
"S" for "scissors".
When the program is run, the user is asked to pick an option between "R", "P" or "S"
If user input is invalid (not amongst the options or an empty input), an error is printed, the user is asked for their input again (loop).

Both player's moves are printed in the format: `Player (Rock) : CPU (Paper)`

If there is a winner, print the winner, and the program ends. 
If it's a tie (the computer and player pick the same move), the game is restarted.