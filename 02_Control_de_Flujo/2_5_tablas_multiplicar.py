"""
Escribe un código que pida al usuario un número entero entre 1 y 10.
A continuación, el programa debe mostrar la tabla de multiplicar completa de ese número (del 1 al 10).

Desafío extra: Al lado de cada resultado, indica si el número es "par" o "impar".
"""
numero = int(input('Dime un numero de 1 A 10'))

for i in range(1, 10):
    if (numero * i) % 2 == 0:
        print(f'{numero} multiplica {i} = {numero * i} Es par' )
    else:
        print(f'{numero} multiplica {i} = {numero * i} Es inpar' )

