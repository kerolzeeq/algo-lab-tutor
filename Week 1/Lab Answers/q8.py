def use_if():
    flag = True
    while flag:
        player1 = eval(input('P1 - Rock[1], Paper[2] or Scissors[3]? '))
        player2 = eval(input('P2 - Rock[1], Paper[2] or Scissors[3]? '))
        
        if (player1==1 and player2==1) or (player1==2 and player2==2) or (player1==3 and player2==3):
            print('DRAW!')
        elif (player1==1 and player2==3) or (player1==3 and player2==2) or (player1==2 and player2==1):
            print('Player 1 WINS')
        elif (player2==1 and player1==3) or (player2==3 and player1==2) or (player2==2 and player1==1):
            print('Player 2 WINS')

        check = input('Do you want to start a new game? [Y,N] : ')
        if check.lower()=='n' :
            flag = False

def use_dict():
    flag = True
    while flag:
        wincheck={'rock':'scissors',
                'scissors':'paper',
                'paper':'rock'}
        player1 = input('P1 - Rock[1], Paper[2] or Scissors[3]? ').lower()
        player2 = input('P2 - Rock[1], Paper[2] or Scissors[3]? ').lower()

        if player1==player2:
            print('DRAW!')
        elif wincheck.get(player1)==player2:
            print('Player 1 WINS!')
        else:
            print('Player2 WINS!')
        check = input('Do you want to start a new game? [Y,N] : ')
        if check.lower()=='n' :
            flag = False

#choose which method want to use

use_if()
# use_dict()