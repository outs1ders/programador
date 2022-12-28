# exercise 1
import random


def string_more_long(a):
    string_long = None
    valor_long = len(a[0])
    num_ls = 0
    for valor in range(len(a)):
        val = len(a[valor])
        if valor_long < val:
            valor_long = val
            num_ls = valor
        string_long = a[num_ls]
    return string_long
    # def main ( print(string_more_long(["hello", "how", "are", "you])) )


# exercise 2

def plus(ls):
    sum = 0
    for number in ls:
        sum += number

    return sum
    # def main ( print(plus([1, 2, 3, 4, 5])) )


# exercise 3


def is_odd(number):
    odd_r = None
    if number % 2 == 1:
        odd_r = True
    else:
        odd_r = False

    return odd_r
    # def main ( print(is_odd(24))


# exercise 4


def sure(question):
    global ans
    if question == "y" or question == "yes":
        ans = True
    elif question == "n" or question == "no":
        ans = False
    return ans


# def main ( print(sure(input("are you sure yes or no ? \n: "))) )

# exercise 5

from string import ascii_uppercase, ascii_lowercase


def switch_to_upper_word(word):
    up = []
    f = []
    a = []
    b = []
    for letter_up in ascii_uppercase:
        a.append(letter_up)
    for letter_lo in ascii_lowercase:
        b.append(letter_lo)
    for letter in word:
        search = b.index(letter)
        up.append(search)
    for letter_f in up:
        fn = a[letter_f]
        f.append(fn)

    str_up = "".join(f)

    return str_up
    # def main ( print(switch_to_upper_word("negro")) )


# exercise 6

def guess_number(a):
    fin = str("well done")
    random_num = random.randint(1, 100)
    while a != random_num:
        a = int(input("enter a number in 1 to 100: "))
    return fin
    # def main( print(guess_number(int(input("enter a number in 1 to 100: ")))) )


# exercise 7

ls = ["pencil", "colors", "pen", "book"]


def add_are_you_sure(a):
    fin = None

    if a in ls:
        fin = str("is already on the list")

    if a not in ls:
        ls.append(a)
        fin = str("has been added")

    return fin


def main():
    print(add_are_you_sure(input("enter one thing for shopping list")))


if __name__ == "__main__":
    main()
