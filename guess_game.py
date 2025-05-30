import random
secret_number = random.randint(1, 10)
guess_count = 0
max_guesses = 4
guess = 0

while guess != secret_number:
    guess_count +=1
    guess = int(input("Guess a secret number (between 1 and 10): "))
print(f"Your guess is {guess}.")