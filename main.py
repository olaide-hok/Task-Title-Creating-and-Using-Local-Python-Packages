# Rock-Paper-Scissors

import random
from unittest import result

while True:
    options=['R', 'P', 'S']

    CPU = random.choice(options)
    Player = None

    while Player not in options:
        # if Player not in options:
        #     print('Error, please type in correct a option')
        #     break
        Player = input('R for Rock, P for Paper, or S for scissors?: ').upper()

    if Player == CPU:
        print('Player {}, CPU {} '.format(Player, CPU))
        print('Tie!')
    
    elif Player == 'R':
        if CPU == 'P':
            print(Player, CPU )
            print('You lose!')
        if CPU == 'S':
            print(Player, CPU )
            print('You win!')
    
    elif Player == 'S':
        if CPU == 'R':
            print(Player, CPU )
            print('You lose!')
        if CPU == 'P':
            print(Player, CPU )
            print('You win!')

    elif Player == 'P':
        if CPU == 'S':
            print(Player, CPU )
            print('You lose!')
        if CPU == 'R':
            print(Player, CPU )
            print('You win!')

    play_again = input('Play again? (yes/no): ').lower()

    if play_again != 'yes':
        break



# import random

# while True:
#     choices = ["rock","paper","scissors"]

#     computer = random.choice(choices)
#     player = None

#     while player not in choices:
#         player = input("rock, paper, or scissors?: ").lower()

#     if player == computer:
#         print("computer: ",computer)
#         print("player: ",player)
#         print("Tie!")

#     elif player == "rock":
#         if computer == "paper":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You lose!")
#         if computer == "scissors":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You win!")

#     elif player == "scissors":
#         if computer == "rock":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You lose!")
#         if computer == "paper":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You win!")

#     elif player == "paper":
#         if computer == "scissors":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You lose!")
#         if computer == "rock":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You win!")

#     play_again = input("Play again? (yes/no): ").lower()

#     if play_again != "yes":
#         break

# print("Bye!")