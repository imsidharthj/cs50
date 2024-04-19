menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
def get_input():
    total = 0
    for item,cost in menu.items():
        print(item, cost, sep = ", ")
    while True:
        try:
            item = input("Item: ").title()
            if item in menu:
                total = total + menu[item]
                print("Total: ",total)
            else:
                print("Invalid input\n")
        except KeyError:
            print("\n")
            continue
        except EOFError:
            print("\n")
            break
    return total

total_cost = get_input()
print(f"${total_cost:.2f}")