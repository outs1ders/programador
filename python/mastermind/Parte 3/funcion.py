"""
def largo_string(mi_string):
    largo = 0
    for n in mi_string:
        largo +=1
    return largo


largo_de_la_string = largo_string("hello to all")
print(largo_de_la_string, )
"""
import math

def main():
    print("quadratic function calculator")
    values = input("enter the values separated by commas : ")
    list_values = [float(number) for number in values.split(",")]

    equation = pow(list_values[1], 2) - 4 * list_values[0] * list_values[2]

    if equation == 0:
        part2_equation = (-list_values[1]) / (2 * (list_values[0]))
        print(part2_equation)

    elif equation < 0:
        print("the equation is very complex")

    elif equation > 0:
        part2_plus = ((-list_values[1]) + math.sqrt(equation)) / (list_values[0] * 2)
        part2_min = ((-list_values[1]) - math.sqrt(equation)) / (list_values[0] * 2)

        print(int(math.sqrt(equation)), "\n", int(part2_plus), "\n", int(part2_min))


if __name__ == "__main__":
    main()


def power(base):
    result = base * base

    return result

base = int(input("ingrese el valor de la base: "))
print(power(base))
