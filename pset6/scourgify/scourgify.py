import sys
import csv
import os

if len(sys.argv) != 3:
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
    else:
        print("Too many command-line arguments")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.isfile(input_file):
    print(f"Could not read {input_file}")
    sys.exit(1)

students = []

with open(input_file, newline='') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        last, first = row['name'].split(', ')
        house = row['house'].strip()
        students.append({"first": first, "last": last, "house": house})

with open(output_file, 'w', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['first', 'last', 'house'])
    writer.writeheader()
    for student in students:
        writer.writerow(student)
