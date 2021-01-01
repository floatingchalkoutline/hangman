import random
from hangman_words import word_list
from oop_word_check import Hangman

hangman = Hangman()

answer = random.choice(word_list)
display = hangman.display_spaces(answer)
lives = hangman.LIVES
guess_list = []

#TODO-1: - Print the logo
print(hangman.LOGO)
print(answer)

play_game = True

while play_game:
    #TODO-2: - Allow for guessing a letter
    print("".join(display))
    guess = input("Guess a letter: ").lower()
    #TODO-3: - Check if letter has already been guessed before
    if guess in guess_list:
        print(f"You have already guessed {guess}. Try again.")
    elif guess not in answer:
        print("Sorry that's incorrect")
        print(hangman.STAGES[lives])
        lives -= 1
        play_game = hangman.check_loss(lives)
    #TODO-4: - Check if letter is in the random word
    elif guess in answer:
        print("Correct")
        display = hangman.modify_answer_display(display, guess, answer)
        play_game = hangman.check_win(display)

    guess_list += guess
