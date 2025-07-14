"""
Escribe un programa que pregunte al usuario su nombre y su sexo.
El programa debe asignar al usuario al Grupo A o al Grupo B según las siguientes reglas:

Grupo A: Mujeres con un nombre que empiece con una letra anterior a la 'M'
(A-L) y hombres con un nombre que empiece con una letra posterior a la 'N' (O-Z).

Grupo B: Todos los demás alumnos.
"""

listA = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
listB = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
grupoA = {}
grupoB = {}

print('Bienvenida al programa de asignación')
nombre = input('Ingrese su nombre: ')
sexo = input('Ingrese su sexo: (f o m)').lower()

if (nombre[0] in listA and sexo == 'f') or (nombre[0] in listB and sexo == 'm'):
    grupoA[nombre] = sexo
else:
    grupoB[nombre] = sexo

print(grupoA, '\n', grupoB)