# Formula de baskara em python
# execute o arquivo e chame a função baskara()

import math

def delta(a, b, c):
        return b ** 2 - 4 * a * c

def baskara():
        a = float(input("Digite o valor da variável a: "))
        b = float(input("Digite o valor da variável b: "))
        c = float(input("Digite o valor da variável c: "))
        print_roots(a, b, c)

def print_roots(a, b, c):
    d = delta(a, b, c)
    if d == 0:
            raiz1 = (-b + math.sqrt(d)) / (2*a)
            print("A única raiz é: ", raiz1)
    else:
            raiz1 = (-b + math.sqrt(d)) / (2 * a)
            raiz2 = (-b - math.sqrt(d)) / (2 * a)
            print("A primeira raiz é: ", raiz1)
            print("A segunda raiz é: ", raiz2)
