listItem = {}
while True:
    try:
        item = input()
        if item in listItem:
            listItem[item] += 1
        else:
            listItem[item] = 1
    except:
        break

order = []

for i in listItem.keys():
    if order == []:
        order.append(i)
    elif order[0][0] > i[0]:
        order.insert(0, i)
    else:
        order.append(i)

for item in order:
    print(f"{listItem[item]} {item.upper()}")
