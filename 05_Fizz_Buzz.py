user_number = int(input('How many times do you want to count? \n'))
i = 0
while i < user_number:
    i += 1
    if i % 3 == 0 and i % 5 == 0:
        print('Fizz Buzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
