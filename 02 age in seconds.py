from datetime import datetime

while True:
    user_age = input('Enter your birth date in format YYYY-MM-DD: ')
    try:
        converted_age = datetime.strptime(user_age, '%Y-%m-%d')
    except Exception:
        print('Wrong date format, try again.')
        continue

    difference = (datetime.now() - converted_age).total_seconds()
    print('Your age is %d seconds.' % difference)
    break
