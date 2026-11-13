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
	print("You LOSSST!!!")
def tie():
	print("You Tied")


if bot == "rock" and player == "rock":
	tie()
elif bot == "rock" and player == "paper":
	player_win()
elif bot == "rock" and player == "scissors":
	bot_win()
elif bot == "paper" and player == "paper":
	tie()
elif bot == "paper" and player == "scissors":
	player_win()
elif bot == "paper" and player == "rock":
	bot_win()
elif bot == "scissors" and player == "scissors":
	tie()
elif bot == "scissors" and player == "rock":
	player_win()
elif bot == "scissors" and player == "paper":
	bot_win()
elif bot == "rock" and player == "Rock":
	tie()
elif bot == "rock" and player == "Paper":
	player_win()
elif bot == "rock" and player == "Scissors":
	bot_win()
elif bot == "paper" and player == "Paper":
	tie()
elif bot == "paper" and player == "Scissors":
	player_win()
elif bot == "paper" and player == "Rock":
	bot_win()
elif bot == "scissors" and player == "Scissors":
	tie()
elif bot == "scissors" and player == "Rock":
	player_win()
elif bot == "scissors" and player == "Paper":
	bot_win()
else:
	print("You LOST!!!!!!")