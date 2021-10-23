import random
from art import *

# Creates 8 Lives
lives = 8

# All Of The HandManX Word Options
wordOptions = ["absurd", "banjo", "cabin", "duplex", "earth", "fjord", "greyhound", "haiku", "ignore", "jackpot", "king", "lambda", "microwave", "nymph", "oxygen", "pigeons", "quartz", "random", "subway", "tailors", "unveil", "vortex", "wave", "xylem", "yarn", "zodiac"]

# Dictionary For Each Of The Characters In The Word
wordChar = {}

# Defines Two Variables Which Pick A Random Word & Find The Length
# Of The Word
word = random.choice(wordOptions)
wordLength = len(word)

# Prints The Length Of The Word And The Number Of Lives
print(f"Length Of Word: {wordLength}")
print(f"Lives: {lives}")

# Fills In Dictionary With _ Equaling Each Character In Words
for i in range(wordLength):
  wordChar[word[i]] = "_"


# Joins The _ Together
print(" ".join(wordChar.values()))
print()
print()

# While Loop Which Keeps Checking If The User Finds The Word Or Not
while(True):
  userInput = input("Choose A Letter: ")
  
  if userInput in wordChar:
    wordChar[userInput] = userInput.upper()
    wordFormed = ("".join(wordChar.values()))
    print(f"Lives: {lives}")
    if wordFormed == word.upper():
      print(wordFormed)
      print("Congrats You Formed The Word!")
      break
  else:
    lives -= 1
    print(f"Lives: {lives}")
    if (lives == 0):
      print("You have no more lives left!")
      print(f"The word was {word.upper()}!")
      break

  print()
  print()    
  print(" ".join(wordChar.values()))

# Prints Logo
tprint("HangManX")
