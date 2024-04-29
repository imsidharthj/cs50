def main():
    text = input("Input: ")
    output = shorten(text)
    print("Output:",output)

def shorten(word):
 vowels = "aeiouAEIOU"
 for vowel in vowels:
  word = word.replace(vowel,"")
 return word

if __name__ == "__main__":
  main()