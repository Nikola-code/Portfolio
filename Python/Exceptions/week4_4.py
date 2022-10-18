#guessing game
import random

while True:
    try:
        n=int(input("Level: "))
    except ValueError:
        continue
    if n<1:
        continue
    else: 
        break
while True:
    try:
        guess=int(input("Guess: "))
    except ValueError:
        continue
    if guess<1:
        continue
    result=random.randint(1,n)
    if guess<result:
        print("Too small!")
    elif guess>result:
        print("Too large!")
    else:
        print("Just right!")
    break
