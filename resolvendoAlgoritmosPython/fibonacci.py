# A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci.
# Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores.
# Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.
n = int(input())
fib_list = []

for i in range(n):
    if (i > 1):
        fib_list.append(fib_list[i-1] + fib_list[i-2])
    else:
        fib_list.append(i)

fib_string = ' '.join([str(x) for x in fib_list])
print(fib_string)