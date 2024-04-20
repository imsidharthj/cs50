def remove_vowels(text):
 vowels = "aeiouAEIOU"
 for vowel in vowels:
  text = text.replace(vowel,"")
 return text

text = input("Input: ")
output = remove_vowels(text)
print("Output:",output)