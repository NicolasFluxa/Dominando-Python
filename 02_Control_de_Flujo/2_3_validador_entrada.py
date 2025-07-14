"""
Escribe un programa que le pida repetidamente al usuario que ingrese una opción
(un número del 1 al 3). El programa no dejará de pedir la opción hasta que el
usuario ingrese un 1, un 2 o un 3. Una vez que se ingrese una opción válida,
el programa la imprimirá en pantalla y terminará.
"""

while True:
    opcion = int(input('Dime 1, 2 o 3'))
    if opcion in [1, 2, 3]:
        print('Correcto una vez mas!')
        break
    else:
        print('Recuerda las opciones!')