def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    x = float(d.replace("$",""))
    return round(x, 1)


def percent_to_float(p):
    x = int(p.replace('%',''))
    return round(x/100,2)


main()
