import random

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break
    except ValueError:
        continue

level = random.randint(1, n)

while True:
    try:
        guess = int(input("guess: "))
        if guess < 0:
            continue
        elif guess < level:
            print("Too small!")
            continue
        elif guess > level:
            print("Too large!")
            continue
        else:
            print("Just right!")
            break
    except ValueError:
        continue