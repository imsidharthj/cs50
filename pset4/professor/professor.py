import random
def main():
    level = get_level()
    score = generate_integer(level)
    print(score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                break
        except ValueError:
            continue
    return level

def generate_integer(level):
    counter = 0
    for i in range(10):
        if level == 1:
            x = random.randint(0, 10**level-1)
            y = random.randint(0, 10**level-1)
        elif level == 2:
            x = random.randint(10, 10**level-1)
            y = random.randint(10, 10**level-1)
        else:
            x = random.randint(100, 10**level-1)
            y = random.randint(100, 10**level-1)
        problem = f"{x} + {y} = "
        result = int(x) + int(y)
        for j in range(3):
            solution = input(problem)
            try:
                solution = int(solution)
                if solution == result:
                    counter = counter + 1
                    break
                else:
                    if j < 2:
                        print(f"EEE")
                    else:
                        print(problem,result)
            except ValueError:
                continue
    return counter

if __name__ == "__main__":
    main()