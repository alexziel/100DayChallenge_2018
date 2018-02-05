import random

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


def play_again():
    while True:
        choose_again = input('Do you want to play again? Yes [y] or no [n]? ').lower()
        if choose_again == 'y' or choose_again == 'yes':
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
        guess = input('Enter your letter: ')
    play_again()


main_game()
