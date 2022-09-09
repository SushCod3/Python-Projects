import random
import string

print('\nRandom Password Generator\n')

characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')


def pass_generator():
    user = int(input('Enter the length of the password you want to generate: '))

    random.shuffle(characters)
    password = []

    for c in range(user):
        password.append(random.choice(characters))

    attach = ''.join(password)
    print(f'\nGenerated Password: {attach}')


pass_generator()

while True:
    print('\nWant to generate another password?')
    user = input('Yes or No\n')
    if user.lower() == 'Yes'.lower():
        pass_generator()
    elif user.lower() == 'no'.lower():
        print('\nHope to see you again!')
        exit()
    else:
        print('Sorry, I can only accept "Yes" or "No"')
        user
