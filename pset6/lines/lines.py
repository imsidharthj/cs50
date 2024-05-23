import sys
import os

if len(sys.argv) != 2:
    if len(sys.argv) > 2:
        print("Too few command-line arguments")
    else:
        print("Too many command-line arguments")
    sys.exit(1)
filename = sys.argv[1]
if not os.path.exists(filename):
    print("File does not exist")
    sys.exit(1)
if not filename.endswith(".py"):
    print("Not a Python file")
    sys.exit(1)
total_lines = 0
with open(filename) as file:
    for line in file:
        lines = line.lstrip()
        if not lines.startswith('#') and lines:
            total_lines = total_lines + 1
print(f"Total lines of code: {total_lines}")
