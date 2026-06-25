import random
print("Welcome to Simple Hangman game")
print("Guess the word")

words = ["apple","penguine","lion","carrot","king"]
secret_word = random.choice(words)
guessed = ["_"] * len(secret_word)

attempt = 6
guessed_letters = []
print(" ".join(guessed))

while attempt > 0 and  "_" in guessed:
    guess = input("\nEnter a Letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter only alphabet letter")
        continue

    if guess in guessed_letters:
        print("\n You have already guessed that letter")
        continue

    guessed_letters.append(guess)
    print("Guessed letters:", guessed_letters)

    if guess in secret_word:
        print("Correct")

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed[i] = guess
        print(" ".join(guessed))
    else:
        attempt -= 1
        print(f"Wrong!! {attempt} attempts left.")
        print(" ".join(guessed))

if '_' not in guessed:
    print("Congratulations!! You Won!")
    print(f"The word was {secret_word}")
else:
    print("Oooppss You Lose! Better Luck next time!!")
    print(f"The word was {secret_word}")                   

    

