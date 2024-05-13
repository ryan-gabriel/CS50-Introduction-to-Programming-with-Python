fraction = input("Fraction: ")
while(True):
    try:
        if "/" not in fraction or "." in fraction or eval(fraction) > 1:
            continue
        else:
            result = round(eval(fraction)*100)
            if result >= 99:
                print("F")
            elif result <= 1:
                print("E")
            else:
                print(f"{int(round(result))}%")
            break

    except:
        continue
