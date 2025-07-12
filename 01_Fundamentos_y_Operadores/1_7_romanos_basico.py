"""
Desarrolla un programa que reciba un número romano como texto y lo convierta a su valor entero.
Para este primer desafío, simplemente suma el valor de cada letra sin preocuparte
por las reglas de sustracción (como 'IV' para 4).
"""

romanos = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}


numero = input('Dime un numero romano').upper()

if len(numero) == 1:
    print(romanos[numero])
else:
    print(romanos[numero[0]], ' ', romanos[numero[1]])

"""
Incorporacion de ciclos para mejorar el codigo

suma_total = 0
for letra in numero:
  # ¿Qué harías aquí con cada 'letra' y la variable 'suma_total'?

print(suma_total)

"""

