import re
import sys


def main():
    print(count(input("Text: ")))

def count(s):
    number_um = re.findall(r"\b\W*um\W*", s, re.IGNORECASE)
    count_um = len(number_um)
    return count_um

if __name__ == "__main__":
    main()