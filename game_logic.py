import random
from ascii_art import STAGES

"""List of secret words"""
WORDS = ["python", "git", "github", "snowman", "meltdown"]
max_attempts = len(STAGES) -1


"""Selects a random word from the list."""
def get_random_word():
    return WORDS[random.randint(0, len(WORDS) - 1)]

""" Displays stages of snowman for current mistakes"""
""" Display guessed letter + mistakes count"""
def  display_game_state(mistakes, secret_word, guessed_letters):
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
    print("Secret word selected: " + secret_word)  # for testing, later remove this line

    """ Game Loop"""
    while attempts < max_attempts:
        display_game_state(attempts, secret_word, guessed_letter)

        if all(letter in guessed_letter for letter in secret_word):
            print("You guessed the word! you win ")
            break

        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or guess not in "abcdefghijklmnopqrstuvwxyz":
                print("please enter a single alphabetical letter (a -z).")
            elif guess in guessed_letter:
                print("You already guess that letter, try again!")
            else:
                break

        """Correct guesses added to guessed_letters"""
        """Runs if input is valid"""
        guessed_letter.add(guess)

        """Mistakes counter for incorrect guess"""
        if guess not in secret_word:
            attempts += 1
            print(f"Incorrect, try again!")
        else:
            print("Nice Guess!")
    else:
         display_game_state(attempts, secret_word, guessed_letter)
         print(f"You are all out of guess and the snowman is melted")



if __name__ == "__main__":
    play_game()

