# Rock-Paper-Scissors

import random

while True:
    options=['R', 'P', 'S']

    CPU = random.choice(options)
    Player = None
    Player = input('R for Rock, P for Paper, or S for scissors?: ').upper()
    while Player not in options and Player != None:
        print('Error, please type in correct a option')
        Player = input('R for Rock, P for Paper, or S for scissors?: ').upper()

    while (Player == CPU):
        print('Player ({}) : CPU ({})'.format(Player, CPU))
        print('Tie!')
        Player = input('R for Rock, P for Paper, or S for scissors?: ').upper()
 
    if Player == 'R':
        Player = 'Rock'
        if CPU == 'P':
            CPU = 'Paper'
            print('Player ({}) : CPU ({})'.format(Player, CPU))
            print('You lose!')
        if CPU == 'S':
            CPU = 'Scissors'
            print('Player ({}) : CPU ({})'.format(Player, CPU))
            print('You win!')
    
    elif Player == 'S':
        Player = 'Scissors'
        if CPU == 'R':
            CPU = 'Rock'
            print('Player ({}) : CPU ({})'.format(Player, CPU))
            print('You lose!')
        if CPU == 'P':
            CPU = "Paper"
            print('Player ({}) : CPU ({})'.format(Player, CPU))
            print('You win!')

    elif Player == 'P':
        Player = 'Paper'
        if CPU == 'S':
            CPU = 'Scissors'
            print('Player ({}) : CPU ({})'.format(Player, CPU))
            print('You lose!')
        if CPU == 'R':
            CPU = 'Rock'            
            print('Player ({}) : CPU ({})'.format(Player, CPU))
            print('You win!')

    play_again = input('Play again? (yes(y)/no(n)): ').lower()

    if play_again != 'yes' or play_again != 'y':
        break
print("Bye!")


