
def ready():
    print('\nSCIENCE QUIZ\n')
    print('Are you ready to answer some questions?')
    ready = input('Yes or No?\n')
    if ready.lower() == 'Yes'.lower():
        print('\nHere goes the first Question:')
    elif ready.lower() == 'no'.lower():
        print('\nHope to see you again!')
        exit()
    else:
        print('Sorry I can only accept "Yes" or "No"')
        ready


ready()


def quiz():
    quiz = {
        'q1': {'q': 'What produces the 50-80% of oxygen on Earth?', 'a': 'Ocean'},
        'q2': {'q': 'What animal do we share 98% of our DNA with?', 'a': 'Chimpanzee'},
        'q3': {'q': 'What theory explains the begining of our universe?', 'a': 'Big Bang Theory'}
    }

    score = 0

    for k, v in quiz.items():
        print('')
        print(v['q'])
        answer = input('Answer: ')
        if answer.lower() == v['a'].lower():
            score = score + 10
            print(f'\nCorrect!!\nThe answer is', v['a'], '.')
            print(f'\nYour score is {score}')
        else:
            print(f'\nWrong Answer!\nThe correct answer is', v['a'], '.')
            print(f'\nYour score is {score}.')
    print(f'You answered {int(score/10)} out of 3 questions correctly.')
    print(f'Your score percertage is {int(score/3) * 10}%.')
    print('\nThanks for your valuable time :)')


quiz()

while True:
    print('\nPlay Again?')
    play_again = input('Yes or No?\n')
    if play_again.lower() == 'Yes'.lower():
        ready()
        quiz()
    else:
        print('\nHope to see you again!')
        exit()
