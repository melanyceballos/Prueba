"Clasificador de temperatura:"
"Necesitamos desarrollar un programa que solicite al usuario una temperatura (en grados Celsius) y mostrar un"
"mensaje dependiendo del rango"
"Menor a 8 Hace mucho frio"
"Entre 0 y 20 Clima templadito"
"Entre 21 y 30 Clima agradable"
"Mayor a 30- Terrible"


temperatura = int(input("Por favor, ingrese la temperatura: "))
if temperatura < 0:
    print("Hace mucho frio")
elif temperatura <= 20:
    print("Clima templadito")
elif temperatura <= 30:
    print("Clima agradable")
else:
    print("La temperatura es Terrible...")