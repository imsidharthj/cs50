import sys
def main():
    text = input("Input: ")
    output = shorten(text)
    print("Output:",output)

def shorten(word):
 vowels = "aeiouAEIOU"
 for vowel in word:
  if vowel in vowels:
    word = word.replace(vowel,"")
  elif vowel in "0123456789":
    sys.exit(1)
 return word

if __name__ == "__main__":
  main()