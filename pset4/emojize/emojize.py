import emoji

emoji_name = input("Input: ")

emoji_type = emoji.emojize(f"Output: {emoji_name}", language='alias')
print(emoji_type)