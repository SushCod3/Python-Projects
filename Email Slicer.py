# Email Slicer

print('\nHello, There!\nWelcome to Email Slicer\n')


def email_slicer():
    email = input('Enter the Email Address: ')
    username, domain = email.split('@')
    domain, extension = domain.split('.')
    print('Username: ', username, '\nDomain: ',
          domain, '\nExtension: ', extension)


email_slicer()

while True:
    print('\nWant to do another?')
    user = input('\nYes or No\n')
    if user.lower() == 'Yes'.lower():
        email_slicer()
    elif user.lower() == 'no'.lower():
        print('\nHope to see you again!')
        exit()
    else:
        print('Sorry I can only accept "Yes" or "No"')
        user
