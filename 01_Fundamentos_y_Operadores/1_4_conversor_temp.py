"""
Desarrolla un programa que funcione como un conversor de temperaturas.
Primero, debe preguntar al usuario qué conversión desea realizar
(opción 1 para Celsius a Fahrenheit, opción 2 para Fahrenheit a Celsius).
Luego, solicitará la temperatura y mostrará el resultado con dos decimales.
"""
opcionTemp = input('A que temperatura te gustaria convertir C o F')

if opcionTemp == 'C':
    temp = float(input('Temperatura en Fahrenheit: '))
    print('La temperatura en grados Celsius es: ', ((temp - 32) * (5/9)))
else:
    temp = float(input('Temperatura en Celsius: '))
    print('La temperatura en grados Fahrenheit es: ', ((temp * 9 / 5) + 32))


"""
Control de los decimales

resultado = (temp - 32) * (5/9)
print('La temperatura en grados Celsius es:', round(resultado, 2))

f-string
resultado = (temp - 32) * (5/9)
print(f'La temperatura en grados Celsius es: {resultado:.2f}')
"""