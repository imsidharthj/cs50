import sys
from tabulate import tabulate
import csv

if len(sys.argv) != 2:
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
    else:
        print("Too many command-line arguments")
    sys.exit()
filename = sys.argv[1]
if not filename.endswith(".csv"):
    print("Not a CSV file")
    sys.exit()

tables = []
with open(filename, newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        tables.append(row)
print(tabulate(tables, headers="firstrow", tablefmt="grid"))