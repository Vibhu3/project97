import random

x = random.randint(1, 10)
chances=0
while chances<5:
  guess = int(input("Enter an integer from 1 to 10: "))

  if guess < x:
    print ("guess is too low")
  elif guess > x:
    print ("guess is too high")
  else:
    print ("CONGRATULATIONS your pick was right")
    break
  chances=chances+1