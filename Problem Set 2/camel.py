def main():
    word = input("camelCase: ")
    snake = ""
    for i in word:
        if i.isupper():
            snake += "_" + i.lower()
        else:
            snake += i
    print("snake_case:",snake)

if __name__ == "__main__":
    main()
