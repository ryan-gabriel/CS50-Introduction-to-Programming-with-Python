text = input("Input: ")
newText = ""
for i in text:
    if i.lower() in ["a","i","u","e","o"]:
        continue
    newText += i

print(newText)
