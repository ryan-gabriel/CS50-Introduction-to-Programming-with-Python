month = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    try:
        date = input("Date: ").strip()

        # Memeriksa apakah input berisi karakter "/"
        if "/" in date:
            month_str, day, year = date.split("/")
            month_index = month.index(month_str)
            if 1 <= int(day) <= 31 and 1 <= month_index + 1 <= 12:
                print(f"{year}-{month_index + 1:02d}-{int(day):02d}")
                break
            else:
                raise ValueError
        else:
            # Memeriksa apakah kata pertama input adalah nama bulan
            if date.split()[0] in month:
                month_str = date.split()[0]
                day = int(date.split()[1].rstrip(","))
                month_index = month.index(month_str)
                if 1 <= day <= 31:
                    print(f"{date.split()[-1]}-{month_index + 1:02d}-{day:02d}")
                    break
                else:
                    raise ValueError
            else:
                raise ValueError
    except ValueError:
        print("Invalid date input.")
