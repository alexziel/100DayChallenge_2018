import random

toss_range = 100
heads = 0
tails = 0

print('Welcome to the Heads/Tails game! For', toss_range, 'tosses, you have:')

for i in range(toss_range):
    flip = random.randint(0, 1)
    if flip == 1:
        heads = heads + 1
    else:
        tails = tails + 1

print(heads, 'heads')
print(tails, 'tails.')