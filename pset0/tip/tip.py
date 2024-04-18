def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(input_str):
    amount_str = input_str.lstrip("$")
    input_flaot = float(amount_str)
    return input_flaot

def percent_to_float(input_str):
    amount_str = input_str.rstrip("%")
    input_float = float(amount_str)/100
    return input_float

main()