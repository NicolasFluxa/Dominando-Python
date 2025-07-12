"""
Crea un programa que pida al usuario tres números enteros.
Luego, debe mostrar en pantalla cuál de los tres es el número más grande y cuál es el más pequeño.
"""

num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa otro numero: "))
num3 = int(input("Ingresa otro numero: "))

numMax = num1

if num1 > num2 and num1 > num3:
    numMax = num1
    if num2 > num3:
        print('El numero mas pequeño es ', num3)
    else:
        print('El numero mas pequeño a ', num2)
elif num2 > num1 and num2 > num3:
    numMax = num2
    if num3 > num1:
        print('El numero mas pequeño a ', num1)
    else:
        print('El numero mas pequeño a ', num3)
else:
    numMax = num3
    if num1 > num2:
        print('El numero mas pequeño a ', num2)
    else:
        print('El numero mas pequeño a ', num1)


print(numMax)


"""
Forma rapida 

numero_maximo = max(num1, num2, num3)
numero_minimo = min(num1, num2, num3)

print(f"El número más grande es: {numero_maximo}")
print(f"El número más pequeño es: {numero_minimo}")
"""
