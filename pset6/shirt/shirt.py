import sys
import os
from PIL import Image, ImageOps
import requests
from io import BytesIO

if len(sys.argv) != 3:
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
    else:
        print("Too many command-line arguments")
    sys.exit(1)

command_input = sys.argv[1].lower()
command_output = sys.argv[2].lower()

valid_extension = lambda filename: filename.endswith(('.jpg', '.jpeg', '.png'))
if not valid_extension(command_input) or not valid_extension(command_output):
    print("Invalid input")
    sys.exit(1)

if os.path.splitext(command_input)[1] != os.path.splitext(command_output)[1]:
    print("Input and output have different extensions")
    sys.exit(1)

if not os.path.exists(command_input):
    print("Input does not exist")
    sys.exit(1)

try:
    photo = Image.open(command_input)
    shirt_url = "https://cs50.harvard.edu/python/2022/psets/6/shirt/shirt.png"
    response = requests.get(shirt_url)
    shirt = Image.open(BytesIO(response.content))
    photo = ImageOps.fit(photo, shirt.size)
    # shirt = shirt.resize(photo.size)
    photo.paste(shirt, (0, 0), shirt)
    photo.save(command_output)
    print(f"{command_output}")

except FileNotFoundError:
    sys.exit(1)