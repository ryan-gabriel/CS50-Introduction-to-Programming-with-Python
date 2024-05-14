import random
import sys

while True:
    try:
        level = int(input("Level: "))
        if level <= 0:
            continue
        else:
            break
    except:
        sys.exit

target = random.randint(1,level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        elif guess == target:
            print("Just right!")
            break
    except:
        sys.exit
