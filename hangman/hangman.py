secret_word = "linux"
tries = 6
guessed_letters = []

while tries > 0:
    guess = input("Guess a letter: ").lower()

    # Win by guessing the whole word
    if guess == secret_word:
        print("🎉 You guessed the word!")
        break

    # Correct letter
    if guess in secret_word:
        if guess not in guessed_letters:
            guessed_letters.append(guess)
        else:
            print("You already guessed that letter!")
    else:
        tries -= 1
        print(f"Wrong! You have {tries} tries left.")

    # Display the word
    for letter in secret_word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

    # Check if every letter has been guessed
    won = True
    for letter in secret_word:
        if letter not in guessed_letters:
            won = False
            break

    if won:
        print("🎉 You guessed every letter! You win!")
        break

if tries == 0:
    print(f"You lost! The word was '{secret_word}'.")
