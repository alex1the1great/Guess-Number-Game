from random import randint

guessed = False
guesses = 0
computer_number = randint(0, 100)  # return a number between 0 to 100

while not guessed:
    user_guess = int(input('Try to guess the number: '))  # type casting
    guesses += 1  # increment guesses by 1

    if user_guess == computer_number:
        print('Congratulations! You guessed it correctly!')
        print(f'It took you {guesses} guesses!')
        break
    elif user_guess > computer_number:
        print('The number is lower than what you guessed.')
    elif user_guess < computer_number:
        print('The number is greater than what you guessed.')
    else:
        print('Error Occur')
