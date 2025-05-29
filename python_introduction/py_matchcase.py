import random 
import time
# This is a simple number guessing game using match-case statement.
def play_game():
    secret_number = random.randint(1, 10)
    guess = int(input("Guess the secret number (between 1 and 10): "))

    match guess:
        case _ if guess == secret_number:
            print("Congratulations, you guessed it!")
        case _ if guess > secret_number:
            print("Oops, your guess is a bit high. Try again later!")
        case _ if guess < secret_number:
            print("Nope, your guess is a bit low. Give it another shot!")
        case _:
            print("Hmm, that's an unexpected guess. Try again!")
   
def main():
    print("Welcome to the Guess the Number Game!")
    time.sleep(2)
    play_game()
    time.sleep(2)
    play_again = ()
    play_again = input("Do you want to play again? (yes/No): ")
    if play_again == "yes":
        print("... new game starts")
        time.sleep(2)
    else:
        print("Thanks for playing! Goodbye!")
        time.sleep(2)
main()