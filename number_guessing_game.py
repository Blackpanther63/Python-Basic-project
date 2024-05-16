import random

def guess_number(player_name):
    print(f"Welcome, {player_name}, to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100.")
    print("Try to guess it!")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try guessing higher.")
        elif guess > secret_number:
            print("Too high! Try guessing lower.")
        else:
            print(f"Congratulations, {player_name}! You guessed the number {secret_number} correctly in {attempts} attempts!")
            break

def main():
    player_name = input("What's your name? ")
    play_again = "yes"
    while play_again.lower() == "yes":
        guess_number(player_name)
        play_again = input("Do you want to play again? (yes/no): ")

    print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    main()
