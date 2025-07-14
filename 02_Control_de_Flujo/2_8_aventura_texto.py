"""
Este es un proyecto para integrar todo lo aprendido.
Crea una breve aventura de texto interactiva. La historia comienza contigo escapando de una prisión.
El juego debe presentar al jugador una situación y luego ofrecer dos o más opciones.
Utilizando condicionales anidados (if/elif/else), la historia debe cambiar y
ramificarse según las decisiones del jugador, llevándolo a diferentes finales.
"""
dato = False

opcion1 = input('tienes la opcion de escapar de la prision la tomas o la dejas s o n')
if opcion1 == 's':
    print('Que empiece el juego')
    print('Dentro de tu camino de huida te enfrentas a uno de tus compañeros')
    opcion2 = input('Decides eliminarlo para que no entorpezca tu hiuda o lo invitas')
    if opcion2 == 's':
        dato = True

    print('En tu camino de huida pasas por un tune en donde debes cruzar pero no estas seguro ')
    if dato:
        print('Como vas con un compañero le dices que pase el primero, pero lamentablemente como hay cocodrilos el termina siendo deborado por ellos, mientras tu compañero es la cena de cocodrilos tu aprovechas el momento y logras huir de la prision, felicidades eres libre')
    else:
        print('Como vas solo y el tunel esta lleno de cocodrilos termina tu huida sindo la cena de muchos cocodrilos')
else:
    print('Te quedan 40 años aun, mucha suerte!')

