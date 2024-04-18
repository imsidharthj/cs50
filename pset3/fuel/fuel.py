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
            print("plese put fraction = X/Y")
            continue
        except ZeroDivisionError:
            print("Y can not be 0")
            continue
     

def get_input():
     fraction = input("Fraction: ")
     numerator,denomenator = fraction.split("/")
     numerator = int(numerator)
     denomenator = int(denomenator)
     percentage = (numerator / denomenator) * 100
     round_percent = round(percentage)
     return round_percent

if __name__ == "__main__":
     value = divide()
     print(value)