def main():

    a = input("What is the Answer to the Great Question of Life, the Universe and Everything ").strip().lower()

    if a == "42":
        print("yes")
    elif a == "forty-two":
        print("yes")
    elif a == "forty two":
        print("yes")
    else:
        print("no")
main()