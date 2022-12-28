# fibonacci recursivo
def fibo(val):
    if val < 2:
        return val
    return fibo(val - 1) + fibo(val - 2)

# fibonacci lineal
def fibonacci(valor):
    a = 0
    b = 1
    for number in range(valor):
        c = a + b
        a = b
        b = c
    return b


def main():
    for numbers in range(3):
        print(fibo(numbers))
if __name__ == "__main__":
    main()

"""    
# powwer my solution
def potencia(base,expo= None):
    if expo == None:
        base = base * base
        return base
    elif expo:
        result=1
        for numero in range(expo):
            result *= base
        return result

# power final solution

def poten(numero, base=2):
    resultado = numero
    for valor in range(1,base):
        resultado *= numero
    return resultado


print(poten(3,4))

"""





