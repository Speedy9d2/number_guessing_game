import random

EASY_LEVEL = 10
HARD_LEVEL = 5



#This will check if the player picked the correct number
def checkAnswer(guess, answer, turns):
    if guess > answer:
        print(f"Your guess of {guess} is too high")   
        return turns - 1
    elif guess < answer:
        print(f"Your guess of {guess} is too low")
        return turns - 1
    else: 
        print(f"Your guess of {guess} is correct, you win")
    
#This will set difficulty level
def setDifficulty():
    userInput = input("Type 'easy' or 'hard' to set difficulty: ")
    if userInput == "easy":
        return EASY_LEVEL
    elif userInput == "hard":
        return HARD_LEVEL

#! This is going to be the game function
def game():    
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  gameAnswer = random.randint(1, 100)
  print(f"psss the answer is {gameAnswer}")
  
  turns = setDifficulty()
 
  #Let the user guess a number
  guess = 0
  while guess != gameAnswer:
    print(f"You {turns} lives left")
    guess = int(input("Make a guess: "))
    turns = checkAnswer(guess, gameAnswer, turns)
    if turns == 0:
        print("You lose, game is over")
        return

game()
