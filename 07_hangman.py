import random
import string

hangman = [
'''
   _____
  |     |
  |
  |
  |
  |
==|=======''',

'''
   _____
  |     |
  |     O
  |
  |
  |
==|=======    
''',

'''
   _____
  |     |
  |     O
  |     |
  |
  |
==|=======    
''',

'''
   _____
  |     |
  |     O
  |    /|
  |
  |
==|=======    
''',

'''
   _____
  |     |
  |     O
  |    /|\ 
  |
  |
==|=======    
''',

'''
   _____
  |     |
  |     O
  |    /|\ 
  |    / 
  |
==|=======    
''',

'''
   _____
  |     |
  |     O
  |    /|\ 
  |    / \ 
  |
==|=======    
'''
]

words = ['computer', 'programming', 'lion', 'smartphone', 'codefights']
secret_word = random.choice(words)
guessed_letters = []
blank_word = []
solved_words = 0

print("\nWelcome to Hangman! Guess the word before the man is hung and you win!")

for letters in secret_word:
    blank_word.append('-')


def user_guess():  # TODO user guessing
    print('user guess')


def play_again():
    while True:
        choose_again = input('Do you want to play again? Yes [y] or no [n]? ')
        if choose_again[0].lower() == 'y':
            main_game()
        else:
            print('Bye!')
            exit()


def main_game():
    max_guesses = 2
    i = 0
    print('You have %d guesses left.' % max_guesses)

    while i < max_guesses:
        i += 1
        while True:
            # print('')
            guess = input('Enter your letter: ')
            if len(guess) == 1:
                if guess in string.ascii_letters:
                    break
                print('Please enter only letters')
            else:
                print('Please enter only one character')
        user_guess()
    play_again()


main_game()
