"""
Crea un juego simple donde la computadora elija un número aleatorio entre 1 y 10.
El programa le pedirá al usuario que adivine el número. Si el usuario acierta,
el programa lo felicitará. Si falla, el programa le dirá que no ha acertado y
le revelará cuál era el número correcto.
"""

import random as rd

numero = rd.randint(1, 10)
text = 'Bienvenido a la maquina de la fortuna, acierta en el numero que estoy pensando y Gana!, 1 A 10'
print(text, '\n', len(text) * '-')

if int(input('Dime tu numero \n')) == numero:
    print('Has Ganado!!')
else:
    print(f'No ha acertado a la fortuna!, el numero era {numero}')