# implement a program that:
# Expects zero or two command-line arguments:
# Zero if the user would like to output text in a random font.
# Two if the user would like to output text in a specific font, 
#----in which case the first of the two should be -f or --font,
#----and the second of the two should be the name of the font.
# Prompts the user for a str of text.
# Outputs that text in the desired font.
# If the user provides two command-line arguments and the first is not -f or --font
#----or the second is not the name of a font, the program should exit via
#----sys.exit with an error message.

from pyfiglet import Figlet
import random
import sys


if __name__=="__main__":
    if len(sys.argv) != 3 and len(sys.argv) != 1:
        print("Invalid usage")
        sys.exit(1)
    figlet = Figlet()
    output = ""
    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
        figlet.setFont(font=font)
    elif len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            print("Invalid usage")
            sys.exit(1)
        font_name = sys.argv[2]
        if font_name not in figlet.getFonts():
            print("Invalid usage")
            sys.exit(1)
        figlet.setFont(font=font_name)
    else:
        print("Invalid usage")
        sys.exit(1)
    input_str = input("Input: ")
    output = figlet.renderText(input_str)
    print("Output: ", output)