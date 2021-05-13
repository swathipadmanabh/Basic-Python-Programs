import random

# Guess the number can be of 2 types, computer can guess and user can guess
# In Computer guess, computer generates a random number between the user given range and user tells if the
# number user has in his mind is correct or not
# In User guess, user guesses the number and computer will have a random number generate between the given range
# and computer tells if the guessed number is correct or not

def user_guess1(x):
    random_num = random.randint(1,x)
    guess_num = 0
    while guess_num != random_num:
        guess_num = int(input(f"Enter a random number between 1 and {x}: "))
        if guess_num > random_num:
            print(f"Sorry, Enter a number lesser than the {guess_num}: ")
        elif guess_num < random_num:
            print(f"Sorry, Enter a number greater than the {guess_num}: ")
        else:
            print(f"Success, the number is {guess_num}")

# user_guess1(10)

def computer_guess(x):
    low = 1
    high = x
    user_gues = ''
    while user_gues != 'c':
        if low == high:
            computer_guess_num = low  # becoz high and low are same
            print(computer_guess_num)
            break
        else:
            print(f"the lower and higher values are {low} and {high}")
            computer_guess_num = random.randint(low,high)
            print(f"Computer guessed number is {computer_guess_num}")
            user_gues = input("Please enter c if the guessed number is correct,"
                              " Please enter h if it's higher,"
                              " Please enter l  if it's lower").lower()

        if user_gues == 'h':
            high = computer_guess_num - 1
        elif user_gues == 'l':
            low = computer_guess_num + 1


computer_guess(10)

