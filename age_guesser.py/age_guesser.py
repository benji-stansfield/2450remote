def get_age():
    name = input("What is your name? ")
    result = 'n'
    while (result != 'y'):
        rand = random.randrange(15, 41)
        age_guess = rand
        print(f"{rand}")
        result = input("Is this your age? ('y' or 'n') ")
        if (result == 'y'):
            print(f"{name} is {age_guess} years old!")
            return
        else:
            print("Rats")
get_age()
    