"""
Escribe un programa que solicite al usuario una palabra o una frase.
El programa debe determinar si el texto introducido es un palíndromo
(es decir, si se lee igual de izquierda a derecha que de derecha a izquierda),
ignorando si es mayúscula o minúscula.
"""
"""
.lower(): Convierte una cadena a minusculas.
.upper(): Convierte una cadena a mayúsculas.
.capitalize(): Convierte la primera letra de una cadena a mayúscula y el resto a minúsculas. 
.title(): Convierte la primera letra de cada palabra en una cadena a mayúscula. 
.swapcase(): Intercambia las mayúsculas por minúsculas y viceversa.
isupper(): Devuelve True si todos los caracteres de la cadena son mayúsculas.
islower(): Devuelve True si todos los caracteres de la cadena son minúsculas. 
"""

palabra = input('Dime una palabra para ver si es palindromo').lower()

if palabra == palabra[::-1]:
    print('El texto es palindromo')
else:
    print('El texto no es palindromo')

