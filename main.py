
from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100.")

difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
random_number = random.randint(1, 101)

lives = 0
def guess_func(lives):
	"""Checks if the user guessed the correct number or not. Takes the number of lives as an argument."""
	while lives > 0:
		print(f"You have {lives} attempts remaining to guess the number.")
		guess = int(input("Make a guess: "))
		if random_number == guess:
			print(f"You got it! The answer was {guess}")
			lives = -1 
		elif random_number > guess:
			print("Too low.")
			lives -= 1
			if lives != 0:
				print("Guess again.")
		elif random_number < guess:
			print("Too high.")
			lives -= 1
			if lives != 0:
				print("Guess again.")

	if lives == 0:
		print("You've run out of guesses, you lose.")
		
	
if difficulty_level == "easy":
	lives = 10
	guess_func(lives)

if difficulty_level == "hard":
	lives = 5
	guess_func(lives)