import random
import sys

def main():
    score = 0
    level = get_level()
    for i in range(10):
        equation = generate_integer(level)

        attempt = 0
        while attempt < 3:
            answer = input(f"{equation[0]} + {equation[1]} = ")
            if answer == str(equation[2]):
                attempt = 1
                break
            else:
                print("EEE")
                attempt +=  1
        if attempt == 3:
            print(f"{equation[0]} + {equation[1]} = {equation[2]}")
        else:
            score += 1
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("level: "))
            if level < 1 or level > 3:
                continue
            else:
                return level

        except:
            continue


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
        z = x + y
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
        z = x + y
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
        z = x + y
    return [x,y,z]


if __name__ == "__main__":
    main()
