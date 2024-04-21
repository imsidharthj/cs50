def grocery_list():
    grocery = {}
    while True:
        try:
            item = input("Enter item: ").upper().strip()
            if not item:
                continue
            grocery[item] += 1
        except KeyError:
            grocery[item] = 1
        except EOFError:
            print("\n")
            break
    return grocery

grocery_dict = grocery_list()
sorted_list = sorted(grocery_dict.keys())
for i in sorted_list:
    print(grocery_dict[i], i)