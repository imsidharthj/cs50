message = "Adieu, adieu, to "
names = []
while True:
    try:
        while True:
            name = input("Name: ")
            if not name:
                break
            names.append(name)
    except EOFError:
        print("\n",end="")
        break

if len(names) == 1:
    message = message + names[0]
elif len(names) == 2:
    message = message + names[0] + " and " + names[1]
else:
    for i in range(len(names) - 1):
        message = message + names[i] + ", "
    message = message + "and " + names[-1]
print(message)
