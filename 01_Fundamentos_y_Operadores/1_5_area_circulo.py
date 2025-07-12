"""
Escribe un código que solicite al usuario el radio de un círculo y calcule su área.
Muestra el resultado en pantalla. Puedes usar 3.14159 como una aproximación de π.
"""

radio = float(input('Dime el radio del circulo: '))

print('El area del circulo es: ', (3.14159* radio ** 2))

"""
Importe de libreria

import math # Esta línea va al inicio del archivo

radio = float(input('Dime el radio del circulo: '))
area = math.pi * (radio ** 2)
print(f'El área del círculo es: {area:.4f}') # Aprovechamos para redondear
"""