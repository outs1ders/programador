# from 1
"""
EXIT = str("exit")
LIST = str("list")


# create a file to save the list items
def file(ls_used):
    name_of_file = input("what do you want the file to be called")
    a = open(name_of_file + ".txt", "w")  # create a new file .txt in write mode
    a.write("\n".join(ls_used))  # write the given instruction
    a.close()  # close the file and save

    return a


# create a input so as not to have to write several times
def question():
    return input("enter the product to add [{} for Exit]")


def main():
    list_buys = []
    list_available = ["pan", "chicken", "tomato"]
    input_user = question()

    while input_user != EXIT:
        if input_user == LIST:
            print("\nproducts available", list_available, "\n")
            input_user = question()

        elif input_user in list_available:
            list_buys.append(input_user)
            print("\n".join(list_buys))
            input_user = question()

        elif input_user not in list_available:
            print("\nthis product not available for enter to the list\n")
            input_user = question()

    file(list_buys)


if __name__ == "__main__":
    main()


# form 2


EXIT = str("exit")
list_items = ["brain", "tomato", "chicken"]


# create a file to save the list items
def file(ls_used):
    name_of_file = input("what do you want the file to be called")
    with open(name_of_file + ".txt", "w") as my_file:
        my_file.write("\n".join(ls_used))


# create a input so as not to have to write several times
def question():
    item_selected = input("enter the product to add [{} for Exit]")
    while item_selected.lower() not in list_items and item_selected != EXIT:
        if item_selected == "list":
            print(list_items)
            item_selected = input("enter the product to add [{} for Exit]")
        else:
            print("this product not available for enter to the list")
            item_selected = input("enter the product to add [{} for Exit]")
    return item_selected


def main():
    list_buys = []
    input_user = question()

    while input_user != EXIT:
        list_buys.append(input_user)
        print("\n".join(list_buys))
        input_user = question()

    file(list_buys)


if __name__ == "__main__":
    main()
"""

# form 3

EXIT = str("exit")
FILE_LIST = "list_buys.txt"


# create a file to save the list items
def file(ls_used):
    with open(FILE_LIST, "w") as my_file:
        my_file.write("\n".join(ls_used))


def save_in_list(list_buys, item_saved):
    if item_saved.lower() in [a.lower() for a in list_buys]:
        print("the product already exist")
    else:
        list_buys.append(item_saved)


# create a input so as not to have to write several times
def question():
    return input("introduce a product |[EXIT] to o out|: ")


# charging the latest list
def charging_or_create_file():
    list_buys = []
    if input("you want to load the latest shopping list? [S/N]") == "s":
        try:
            with open(FILE_LIST, "r") as a:
                list_buys = a.read().split("\n")
        except FileNotFoundError:
            print("File not found")
    return list_buys


def show_list(list_buys):
    print("\n".join(list_buys))


def main():
    list_buys = charging_or_create_file()
    show_list(list_buys)
    input_user = question()

    while input_user != EXIT:
        save_in_list(list_buys, input_user)
        show_list(list_buys)
        input_user = question()

    file(list_buys)


if __name__ == "__main__":
    main()
