"""
Diseña un programa que simule la taquilla de un zoológico.
El programa debe ejecutarse en un bucle continuo para atender a múltiples clientes.
Para cada cliente, debe preguntar la edad y si posee algún tipo de carnet
(Estudiante, Pensionista, Familia Numerosa o Ninguno).
El programa debe aplicar e imprimir las siguientes reglas de descuento:
Menores de 10 años entran gratis.
Entre 25 y 35 años con carnet de Estudiante, tienen un 20% de descuento.
Mayores de 35 y menores de 65 con carnet de Familia Numerosa, tienen un 5% de descuento por integrante.
Mayores de 65 años con carnet de Pensionista, tienen un 25% de descuento.
Mayores de 65 años sin carnet de Pensionista, tienen un 15% de descuento.
Para todos los demás casos, no hay descuento.
"""
texto = ' Bienvenido al zoológico'
print(texto, '\n', (len(texto)-1) * '-')

descuento = input('Tienes algun carnet de descuento').lower()
edad = int(input('Edad: '))

while True:
    if edad <= 10:
        print('Ingreso liberado')
    elif 25 <= edad <= 35 and descuento == 'estudiante':
        print('Ingresa con un 20% de descuento')
    elif edad >= 65 and descuento == 'pensionista':
        print('Ingresa con un 25% de descuento')
    elif 35 < edad < 65 and descuento == 'familia':
        print('Ingresa con un 5% de descuento por integrante')
    elif edad >= 65:
        print('Ingresa con un 15% de descuento')
    elif edad == -22:
        break
    else:
        print('No tienes ningun descuento')




