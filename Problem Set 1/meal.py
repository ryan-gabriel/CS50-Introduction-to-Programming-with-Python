def main():
    x = input("What time is it? ")

    hour, minute = x.split(':')

    if hour == '7' or (hour == '8' and minute == '00'):
        print("breakfast time")
    elif hour == '12' or (hour == '13' and minute == '00'):
        print("lunch time")
    elif hour == '18' or (hour == '19' and minute == '00'):
        print("dinner time")

def convert(time):
    hour, minute = time.split(":")
    minute_decimal = int(minute) / 60
    return str(int(hour) + minute_decimal)

if __name__ == "__main__":
    main()
