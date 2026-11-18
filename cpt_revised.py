#Connor and Sai
import random

def player_input(rock):
		return rock

def player_win():
	print("You Won :)")

def bot_win():
	print("Bot wins")

def tie():
	print("You Tied")

running = True

playerwin = 0

botwin = 0


while running:
	answer = input("Want to play Rock, Paper, Or Scissors? (yes/no): ").lower()

	if answer == "no":
		print("Goodbye!")
		print("You won:", playerwin)
		print("You lost:", botwin)
		running = False
	elif answer == "yes":
		player = player_input(input("Choose Rock, Paper, or Scissors: ").lower())
		list = ["rock", "paper", "scissors"]
		list2 = ["rock", "paper", "scissors"]
		if player not in list2:
			print("Please type rock, paper, or scissors.")
			continue

		bot = random.choice(list)
		print()
		print("The Bot chose:", bot)
		print()

		if bot == "rock" and player == "rock":
			tie()
		elif bot == "rock" and player == "paper":
			player_win()
			playerwin += 1 
		elif bot == "rock" and player == "scissors":
			bot_win()
			botwin += 1 
		elif bot == "paper" and player == "paper":
			tie()
		elif bot == "paper" and player == "scissors":
			player_win()
			playerwin += 1 
		elif bot == "paper" and player == "rock":
			bot_win()
			botwin += 1 
		elif bot == "scissors" and player == "scissors":
			tie()
		elif bot == "scissors" and player == "rock":
			player_win()
			playerwin += 1 
		elif bot == "scissors" and player == "paper":
			bot_win()
			botwin += 1 
		
	else:
		print("Please type yes or no.")
 
