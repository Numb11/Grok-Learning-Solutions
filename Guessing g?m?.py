play = True
print("What is my favourite food?")
while play == True:
  guess = input("Guess? ")
  if guess == "electricity":
    print ("You guessed it! Buzzzz")
    play = False
  else:
    print("Not even close.")
