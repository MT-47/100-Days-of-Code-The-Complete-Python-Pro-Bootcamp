#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from random import randint
from art import logo

def game():
    print(logo)
    game_ON = True

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    Number = randint(1, 100)
    # print(Number)

    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        lives = 10
    else:
        lives = 5
    
    while game_ON:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > Number:
            print("Too high.")
            lives -= 1
        elif guess < Number:
            print("Too low.")
            lives -= 1
        else:
            print(f"You got it! The answer was {Number}.")
            game_ON = False
        
        if lives == 0:
            print("You've run out of guesses, you lose.")
            game_ON = False
        elif guess != Number:
            print("Guess again.")

game()