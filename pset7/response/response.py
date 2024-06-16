from validator_collection import validators
from validator_collection import checkers
def main():
    print(validate(input("What's your email address? ")))

def validate(email):
    try:
        valid_email = checkers(email)
        print("Valid")
    except:
        print("Invalid")

if __name__ == "__main__":
    main()