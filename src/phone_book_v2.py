phone_book = {}
while True:
    command = int(input("Command (1 search, 2 add, 3 quit): "))
    if command == 1:
        name = input("name: ")
        if name in phone_book:
            for n in phone_book[name]:
                print(n)
        else:
            print("no number")
    if command == 2:
        name = input("name: ")
        number = input("number: ")
        if name not in phone_book:
            phone_book[name] = number.split()
            print("ok!")
        else:
            phone_book[name].extend(number.split())
            print("ok!")
#    print(phone_book)
    if command == 3:
        print("quitting...")
        break 