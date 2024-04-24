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

def check_font(text):
    figlet = Figlet()
    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
        figlet.setFont(font=font)
        return figlet.renderText(text)
    elif len(sys.argv) == 3:
        if sys.argv[1].lower() in ("-f", "--font"):
            font_name = sys.argv[2]
            if font_name in figlet.getFonts():
                figlet.setFont(font=font_name)
                return figlet.renderText(text)
            else:
                print(f"Error: '{font_name}'")
                sys.exit(1)
        else:
            print(f"Error: ")
            sys.exit(1)
    else:
        print("Error")
        sys.exit(1)

if __name__=="__main__":
    input_str = input("Input: ")
    change_font = check_font(input_str)
    print("Output: ", change_font)