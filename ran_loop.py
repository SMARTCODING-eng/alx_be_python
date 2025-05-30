import random
seceret_number = random.randint(1, 10+1)
guess = int(input("Guess a secret number (between 1 and 10): "))
if guess == seceret_number:
    print("Congratulations, your guess is right!")
else:
    print("Sorry! Your guess is wrong.")
    print("The secreet number was: ", seceret_number)