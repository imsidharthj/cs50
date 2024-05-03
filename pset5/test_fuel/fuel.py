def main():
    fraction = input("Fraction: ")
    percent = 0
    while True:
        try:
            percent = convert(fraction)
            break
        except (ValueError,ZeroDivisionError):
            fraction = input("Fraction: ")
    print(gauge(percent))

def convert(fraction):
    numerator,denomenator = fraction.split("/")
    numerator = int(numerator)
    denomenator = int(denomenator)
    if denomenator == 0:
        raise ZeroDivisionError
    if not numerator == int(numerator) and denomenator == int(denomenator):
        raise ValueError
    if numerator > denomenator:
        raise ValueError
    percentage = (numerator / denomenator) * 100
    round_percent = round(percentage)
    return round_percent
    
def gauge(percent):
    if percent <= 1:
        return "E"
    elif percent >= 99:
        return "F"
    else:
        return f"{percent:.0f}%"
          
if __name__ == "__main__":
    main()