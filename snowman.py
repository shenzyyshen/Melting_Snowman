import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]
max_attempts = 6

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()
    guessed_letter = set()
    attempts = 0

    print("Welcome to Snowman Meltdown!")
   # print("Secret word selected: " + secret_word)  # for testing, later remove this line

    # TODO: Build your game loop here.
    """ Game Loop"""
    while attempts < max_attempts:
        display_word = [letter if letter in guessed_letter else "_" for letter in secret_word]
        print("current word:" , " ".join(display_word))

        if "_" not in display_word:
            print("You guessed the word! you win!")
            break

        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)

        if guess not in secret_word:
            attempts += 1
            print(f"Incorrect, try again!")

        else:
            print("You are all out of guessed! the word was: ", secret_word)

    # print("would you like to play again:"(y/n))

if __name__ == "__main__":
    play_game()
