def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # user = input{"""Enter the valid-plate that you would like. 
    # Please keep it between 2 and 6 characters(letters or numbers). 
    # Do not use periods, spaces, or punctuation in your vanity-plate
    # letters at start and numbers at the end.(The first number used cannot be a ‘0’.)}
    half_length = len(s) // 2
    first_half = s[:half_length]
    second_half = s[half_length:]
    if (1 <= len(first_half) <= 3 and first_half.isalpha() and first_half.isupper()) and (
        1 <= len(second_half) <= 3 and second_half.isnumeric()) and (
        second_half[0] != '0'):
        return True
    else:
        return False
    
main()