import random
Digits = 0
# the people are dumb code
while Digits == 0:
  Difficulty = int(input("Easy(1), or Hard(2) "))
  if Difficulty == 1:
    Digits = 4
  elif Difficulty == 2:
    Digits = 5
  else:
    Digits = 0
    print("no it must be 1 or 2, try again.")

#genorate the Big number
FinalGuess = str(random.randint(0,(10**Digits)-1))
# add zeros incase number is not 4 digits or more
for i in range(0, Digits-len(FinalGuess)):
  FinalGuess = "0"+FinalGuess

#debug line
print(FinalGuess)

Guesses = 0
PlayerGuess = 0

while PlayerGuess != FinalGuess:
  PlayerGuess = input("What is your guess? ")
  CorrectNum = 0
  for i in range(0,len(FinalGuess)):
    if FinalGuess[i] == PlayerGuess[i]:
      CorrectNum += 1
  if CorrectNum != 4:
    print("you have",CorrectNum,"Correct Numbers")
    Guesses += 1
  else: 
    print("Congratz, it took you",Guesses,"Guesses")