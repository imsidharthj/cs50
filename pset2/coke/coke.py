COCA = 50
due_amount = COCA
while due_amount > 0:
  print("Amount Due: ", due_amount)
  coin = int(input("Insert Coin: "))
  denominations = [25, 10, 5]
  if coin in denominations:
    due_amount = due_amount - coin
  else:
    print("Accept Only Denominations: 25 cents, 10 cents, 5 cents")

print("Change Owed: ", -1 * due_amount)