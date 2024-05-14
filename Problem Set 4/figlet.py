from pyfiglet import Figlet
import sys
import random

lenSys = len(sys.argv)
figlet = Figlet()
listFont = figlet.getFonts()
if lenSys != 1 or lenSys != 3 or (lenSys == 3 and ((sys.argv[1] != "-f" and sys.argv[1] != "--font") or sys.argv[2] not in listFont)):
    print("Invalid usage")
    sys.exit(1)

userInput = input("Input: ")
if len(sys.argv) == 1:
    randomFont = random.choice(listFont)
    figlet.setFont(font=randomFont)
    print(figlet.renderText(userInput))
else:
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(userInput))
