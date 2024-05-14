words = ["Adieu", "adieu"]

try:
    while True:
      word = input("Name: ")
      words.append(word)
except:
    words[2] = "to " + words[2]
    temp = []
    if len(words) == 3:
        for i in words:
            temp.append(i + ", ")
        temp[-1] = temp[-1].replace(", ","")
        print("".join(temp))
    else:
        words[-1] = "and " + words[-1]

        if len(words) == 4:
            for i in words:
                temp.append(i + ", ")
            temp[-1] = temp[-1].replace(", ","")
            temp[2] = temp[2].replace(", ", " ")
        else:
            for i in words:
                temp.append(i + ", ")
            temp[-1] = temp[-1].replace(", ","")

        print("".join(temp))

