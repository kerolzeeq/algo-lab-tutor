import random

ran_num = random.randint(1,9)
guess = eval(input('Guess the random number : '))

if guess==ran_num:
    print('Exactly RIGHT!')
elif guess<ran_num:
    print(f'You guessed too LOW, its {ran_num}')
elif guess>ran_num:
    print(f'You guessed too HIGH, its {ran_num}')