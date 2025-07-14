"""
Desarrolla un programa que pida al usuario que escriba una frase.
El programa deberá analizar el texto y contar cuántas letras mayúsculas,
espacios, comas y puntos hay en total. Al final, debe imprimir el recuento de cada uno.
"""

text = input('Ingresa una frase: ')
todo = {'espacio': 0, 'comas': 0, 'puntos': 0, 'mayusculas': 0}


for letra in text:
    if ' ' in letra:
        todo['espacio'] += 1
    elif ',' in letra:
        todo['comas'] += 1
    elif '.' in letra:
        todo['puntos'] += 1
    elif letra.isupper():
        todo['mayusculas'] += 1

print(todo)