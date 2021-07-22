# Crie um programa que leia um número e mostre os números pares até esse número, inclusive ele mesmo.
x = int(input())

for i in range(x+1):
    if ( i%2 == 0 and i > 0 ):
        print(i)