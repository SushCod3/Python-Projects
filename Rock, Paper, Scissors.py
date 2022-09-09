import random as r


def play():
    # 'r' = Rock, 'p' = Paper, 's' = Scissors
    user = input('\nChose from Rock (r), Paper (p) or Scissors (s) or Exit (x)\n: ')
    computer = r.choice(['Rock', 'Paper', 'Scissors'])

    # r > s, s > p, p > r
    if (user == 's' and computer == 'Scissors') or (user == 'r' and computer == 'Rock') or (user == 'p' and computer == 'Paper'):
        print(f'\nIt\'s a Draw!\nThe computer has chosen {computer}')
    elif (user == 'r' and computer == 'Scissors') or (user == 's' and computer == 'Paper') or (user == 'p' and computer == 'Rock'):
        #user_score += 1
        print(f'\nYou win! \nThe computer has chosen {computer}.')
    elif user == 'x':  # Exit function
        print('\nThe game has ended.\n')
        exit()
    else:
        print(f'\nYou lost \nThe Computer has chosen {computer}')


while True:
    play()
