import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]
max_attempts = len(STAGES) -1

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def  display_game_state(mistakes, secret_word, guessed_letters):
    """ Displays stages of snowman for current mistakes"""
    print(STAGES[mistakes])
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_"

    print("word:", display_word.strip())
    print("Guessed Letters:", " ".join(sorted(guessed_letters)))
    print(f"Mistakes: {mistakes}/ {max_attempts}")


def play_game():
    secret_word = get_random_word()
    guessed_letter = set()
    attempts = 0

    print("Welcome to Snowman Meltdown!")
   # print("Secret word selected: " + secret_word)  # for testing, later remove this line

    # TODO: Build your game loop here.
    """ Game Loop"""
    while attempts < max_attempts:
        display_game_state(attempts, secret_word, guessed_letter)

        if all(letter in guessed_letter for letter in secret_word):
            print("You guessed the word! you win ")
            break


        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)

        if guess in guessed_letter:
            print("You already guess that letter, try again!")
            continue

        guessed_letter.add(guess)

        if guess not in secret_word:
            attempts += 1
            print(f"Incorrect, try again!")

        else:
            print("Nice Guess!")

        if all(letter in guessed_letter for letter in secret_word):
            print("You saved the Snowman! The word was:", secret_word)
            break

    else:
        display_game_state(attempts, secret_word, guessed_letter)
        print(f"You are all out of guesses and the Snowman is melted. The word was: {secret_word}")


    # print("would you like to play again:"(y/n))

if __name__ == "__main__":
    play_game()

