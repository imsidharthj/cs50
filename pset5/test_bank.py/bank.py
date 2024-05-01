def main():
    greeting = input("Greeting: ").strip().lower()
    r_greeting = value(greeting)
    print("$", r_greeting, sep="")

def value(greeting):
    if greeting.lower().startswith("hello"):
        return 0
    elif greeting.lower().startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()