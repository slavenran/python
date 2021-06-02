import random
import time

a = 0
b = 0

while True:
    num_str = input('Number range, in a format a, b, or enter quit: ')
    if num_str == 'quit': quit()
    numbers = num_str.split(',')

    try:
        a = int(numbers[0])
        b = int(numbers[1])
        print(a, b)
        break
    except:
        print('You must enter only numbers and in a proper format.')
        continue

print('Picking a random number...\n')
time.sleep(2)
random_num = random.randint(a, b)
print('Random number picked, you can start guessing!\n')

hint = ''
if random_num % 2 == 0: hint += 'divisible by 2, '
else: hint += 'not divisible by 2, '
if random_num % 3 == 0: hint += 'divisible by 3, '
else: hint += 'not divisible by 3, '
if random_num % 5 == 0: hint += 'divisible by 5, '
else: hint += 'not divisible by 5, '

if hint != '':
    print(f'Hint: The number is {hint[:len(hint)-2]}.')

score = 100
guess_no = 0
while True:
    guess = input('Your guess: ')
    try:
        guess = int(guess)
    except:
        print('You must only enter numbers.')
        continue

    guess_no += 1

    if guess == random_num:
        print(f'You guessed it! The random number was {random_num}!')
        break
    elif guess_no % 10 == 0:
        print('BIG HINT')
    elif guess < random_num:
        if random_num - guess > 50: print('Go much higher')
        elif random_num - guess > 10: print('Go higher')
        else: print('Go just a bit higher')
    elif guess > random_num:
        if guess - random_num > 50: print('Go much lower')
        elif guess - random_num > 10: print('Go lower')
        else: print('Go just a bit lower')
    score -= 1

print(f'Your final score is {score} out of 100!')