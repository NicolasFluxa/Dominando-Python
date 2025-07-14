"""
Crea un programa que solicite al usuario su nombre y un número entero.
Utilizando un bucle for, el programa deberá imprimir el nombre del usuario
en la pantalla tantas veces como indique el número introducido.
"""
nombre = input('Ingresa tu nombre: ')
numero = int(input('Ingresa tu numero: '))

for i in range(numero):
    print(f'{i + 1} su nombre es {nombre}')