expression = input("expression: ")

x,y,z = expression.split(" ")

result = 0
if y == "+":
   result = int(x) + int(z)
elif y == "-":
   result = int(x) - int(z)
elif y == "*":
   result = int(x) * int(z)
elif y == "/":
   result = int(x) / int(z)
else:
   result = None
print(f"{result:.1f}")