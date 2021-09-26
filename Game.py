import random

user_guess = int(input('Guess a number between 1 - 10\nEnter number here: '))
random_number = random.randint(1, 10)

attempt = 1

if user_guess == random_number:
    print(f'The answer is: {random_number}\nWell done, you are correct!\nYou got it in {attempt} attempt.')
    exit()
elif random_number >= user_guess:
    print('Well... you are wrong I will give you a hint. The number is larger than your last attempt try again.')
elif random_number <= user_guess:
    print('Well... you are wrong I will give you a hint. The number is smaller than your last attempt try again.')

attempt = 2

user_guess = int(input('Well guess again...\nEnter number here between 1-10: '))

if user_guess == random_number:
    print(f'The answer is: {random_number}\nWell done, you are correct!\nYou got it in {attempt} attempt.')
    exit()
else:
    print('Well... you are wrong I will give you ANOTHER hint.')
    print('The number is even') if random_number % user_guess == 0 else print('The number is odd')

print('Really, I guess you have bad luck. No more hints try again.')

attempt = 3

while user_guess != random_number:
    user_guess = int(input('Enter number: '))
    if user_guess == random_number:
        print(f'Well done, finnaly it only took you {attempt} attempts.')
    else:
        print('Wrong try again.')
        attempt = attempt + 1
    if attempt >= 10:
        print('Really took you over 10 attempts? Go sleep!')
        exit()
