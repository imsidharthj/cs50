def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if (len(s) < 2) or (len(s) > 6):
        return False
    if not s[:2].isalpha():
        return False
    count_numbers = 0
    for i in s[2:]:
        if i.isdigit():
            count_numbers = count_numbers + 1
        if count_numbers == 1 and i == '0':
            return False
        if count_numbers >= 1 and (not i.isdigit()):
            return False
        if (not i.isalpha()) and (not i.isdigit()):
            return False 

    return True

if __name__ == "__main__":
    main()