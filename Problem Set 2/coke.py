amount = 0
price = 50

while amount < price:
    print(f"Amount Due: {price - amount}")

    user_input = int(input("Insert Coin: "))
    if user_input in [5,10,25]:
        amount += user_input

print(f"Change Owed: {abs(amount - price)}")
