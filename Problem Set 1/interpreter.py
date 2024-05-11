x = input("Expression: ")
result = str(eval(x))
print(result + '.0' if "." not in result else result)
