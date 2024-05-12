def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    numberBefore = False
    otherZero = False
    for i,c in enumerate(s):
        if(c.isdigit()):
            if (c != "0"):
                otherZero = True
            elif(c == "0" and otherZero == False):
                return False
            numberBefore = True

        if c.isdigit() == False and numberBefore:
            return False

    if len(s) > 6 or len(s) <= 2 or "!" in s or " " in s or "." in s:
        return False

    return True


main()
