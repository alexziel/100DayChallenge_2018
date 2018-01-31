import random

guesses = 6
secret_number = random.randint(1, 101)
win = False

print('Welcome to the Higher/Lower game!')
print('Your job is to guess the number from 1 to 100. You have 6 guesses.')

while guesses > 0:
    guess = int(input('Your guess: '))
    guesses -= 1

    if guess > secret_number:
        print('Your guess is too high. You have', guesses, 'guesses remaining.')
    elif guess < secret_number:
        print('Your guess is too low. You have', guesses, 'guesses remaining.')
    else:
        print('You won!')
        win = True
        guesses = 0

if not win:
    print('Sorry, you lose. The number was ', secret_number)

