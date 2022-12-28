EXIT = str("exit")


def question():
    return input("enter the product to add [{} for Exit]")


def main():
    list_buys = []
    input_user = question()

    while input_user != EXIT:
        list_buys.append(input_user)
        print("\n".join(list_buys))
        input_user = question()

    a = open("bought.text", "w")
    a.write("\n".join(list_buys))
    a.close()


if __name__ == "__main__":
    main()
