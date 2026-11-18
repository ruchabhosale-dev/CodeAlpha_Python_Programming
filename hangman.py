
import random

# List of predefined words
words = ["python", "computer", "apple", "coding", "program"]

# Select a random word
secret_word = random.choice(words)

# Variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("Welcome to Hangman Game!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

# Game loop
while incorrect_guesses < max_attempts:

    # Display the word with guessed letters
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the word is completely guessed
    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You guessed the word:", secret_word)
        break

    # Take input from user
    guess = input("Guess a letter: ").lower()

    # Check input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    # Check the guessed letter
    if guess in secret_word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")
        print("Remaining attempts:", max_attempts - incorrect_guesses)

# Check game result
if incorrect_guesses == max_attempts:
    print("\nGame Over!")
    print("The correct word was:", secret_word)
