#Connor and Sai

import random

def player_input(rock):
	return(rock)

player = player_input(input("Choose Rock, Paper, or Scissors:"))
list = ["rock", "paper", "scissors"]
bot = random.choice(list)
print()
print("The Bot chose:", bot)
print()

def player_win():
	print("You Won :)")
def bot_win():
	print("You Lost :(")
def tie():
	print("You Tied")

if bot == "rock" and player == "rock" or "Rock":
	tie()
elif bot == "rock" and player == "paper" or "Paper":
	player_win()
elif bot == "rock" and player == "scissors" or "Scissors":
	bot_win()
elif bot == "paper" and player == "paper" or "Paper":
	tie()
elif bot == "paper" and player == "scissors" or "Scissors":
	player_win()
elif bot == "paper" and player == "rock" or "Rock":
	bot_win()
elif bot == "scissors" and player == "scissors" or "Scissors":
	tie()
elif bot == "scissors" and player == "rock" or "Rock":
	player_win()
elif bot == "scissors" and player == "paper" or "Paper":
	bot_win()
else:
	print("Type Rock, Paper, or Scissors")
	