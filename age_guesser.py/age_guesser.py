import random

# main function to run
def get_age():
    name = input("What is your name? ")
    result = 'n'

    # while loop to make sure it doesn't end until it is right
    while (result != 'y'):
        age_guess = random.randrange(15, 41)
        print(age_guess)
        result = input("Is this your age? ('y' or 'n') ")

        if (result == 'y'):
            print(f"{name} is {age_guess} years old!")
            return
        else:
            print("Rats")

get_age()
