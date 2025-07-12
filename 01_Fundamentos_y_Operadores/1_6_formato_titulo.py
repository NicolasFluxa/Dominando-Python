"""
Crea un programa que defina una variable con un título, por ejemplo,
titulo = "Mi Programa Increíble". Luego, imprime ese título y, justo debajo,
una línea de guiones (-) que tenga exactamente la misma longitud que el título.
En el mismo script, define una variable numérica y muéstrala en pantalla usando una f-string.
"""

titulo = input('Dime un titulo para tu codigo')

print(f'El titulo es el Siguiente: ')
print(f'{titulo}\n{'-' * len(titulo)}')