import random

choice_elements = ['r', 'p', 's']
win_conditions = ['sp', 'pr', 'rs']
statistics = {'win': 0, 'lose': 0, 'tie': 0}

print('Welcome to Rock/Paper/Scissors game.')


def game():
    turns = int(input('How many turns do you want to play? \n'))  # TODO check if it is a number
    i = 0
    while i < turns:
        i += 1
        print('*** Round %d ***' % i)
        comp_choice = choice_elements[random.randrange(0, 3)]
        user_choice = input('Pick rock [r], paper [p] or scissors [s]: \n')  # TODO check if it is a correct letter
        user_choice = user_choice.lower().strip()

        if user_choice in choice_elements:
            if user_choice == comp_choice:
                print('Its a tie! Computer also chose %s' % comp_choice)  # TODO print whole word instead of a letter
                statistics['tie'] = statistics['tie'] + 1
            elif user_choice+comp_choice in win_conditions:
                print('You win! Computer chose: %s' % comp_choice)
                statistics['win'] = statistics['win'] + 1
            else:
                print('You lose. Computer chose %s' % comp_choice)
                statistics['lose'] = statistics['lose'] + 1


def final_stats():
    print('\n*** FINAL STATS: ***')
    print('Wins: %d,\nloses %d,\nties: %d.'
          % (statistics['win'], statistics['lose'], statistics['tie'])
          )


while True:
    game()
    final_stats()
    play_again = input('Press ENTER to continue or q to quit: \n')
    if play_again == 'q':
        break
print('Bye!')

