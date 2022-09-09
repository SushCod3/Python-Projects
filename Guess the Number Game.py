import random as r  # random let's us use the random library of python
# Using 'as r' will let us just write r when we want to access random and it will work

# User
def guess(x):
    random_number = r.randint(1, x)
    guess = 0  # The initial variable for our input guess
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 to {x}: '))
        if guess > random_number:
            print('The number is too high!')
        elif guess < random_number:
            print('The number is too low')
    print(f"Yay! You guessed the {random_number} correctly!")

guess(10)

# Computer
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = r.randint(low, high)
        feedback = input(
            f'Is the guess {guess} correct(C)? Too high (H) or Too low(L)').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print('Please chose from high(H), low(L) or correct(C)')

    print("Yay! The Computer guessed the number {guess} correctly!")


# computer_guess(10)
