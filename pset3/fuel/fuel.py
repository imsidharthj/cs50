def divide():
    while True:
        try:
            percent = get_input()
            if percent <= 1:
                return "E"
            elif percent >= 99:
                    return "F"
            else:
                return f"{percent:.0f}%"
          
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
     

def get_input():
     while True:
        fraction = input("Fraction: ")
        numerator,denomenator = fraction.split("/")
        numerator = int(numerator)
        denomenator = int(denomenator)
        percentage = (numerator / denomenator) * 100

        if percentage > 100:
            continue

        round_percent = round(percentage)
        return round_percent

if __name__ == "__main__":
     value = divide()
     print(value)