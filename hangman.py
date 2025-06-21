import random

def hangman():
    words = ['apple', 'banana', 'grape', 'orange', 'peach']
    word = random.choice(words)
    guessed_letters = []
    tries = 6
    display_word = ['_' for _ in word]

    print("Welcome to Hangman!")
    print("Guess the word, one letter at a time.")

    while tries > 0 and '_' in display_word:
        print("\nWord: " + ' '.join(display_word))
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    display_word[index] = guess
            print("Good guess!")
        else:
            tries -= 1
            print(f"Wrong guess. Tries left: {tries}")

    if '_' not in display_word:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame over. The word was:", word)

if __name__ == "__main__":
    hangman()
