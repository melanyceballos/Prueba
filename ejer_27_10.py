#vaidar si una persona es mayor de edad
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Eres mayor de edad.")       
else:
    print("Eres menor de edad.")
    

"""
Ejercicios:

1. Número positivo, negativo o cero

Descripción: Solicitar un número e indicar si es positivo, negativo o cero.

"""
num = int(input("Ingrese un número: "))
if num > 0:
    print("El número es positivo.")
elif num < 0:
    print("El número es negativo.")     
else:
    print("El número es cero.")

"""

2. Clasificador de notas

Descripción: El usuario ingresa una nota de 0 a 100. Mostrar el nivel académico según el puntaje.

| Rango  | Mensaje   |
| ------ | ----------|
| 90–100 | Excelente |
| 70–89  | Aprobado  |
| 0–69   | Reprobado |

"""
nota = int(input("Ingrese su nota (0-100): "))

if 90 <= nota <= 100:
    print("Excelente")  
elif 70 <= nota <= 89:
    print("Aprobado")
else:
    print("Reprobado")
    
"""
3. Clasificador de edad

Descripción: Pedir la edad del usuario y clasificarla en rangos.

| Rango | Mensaje      |
| ----- | ------------ |
| 0–12  | Niño         |
| 13–17 | Adolescente  |
| 18–59 | Adulto       |
| 60+   | Adulto mayor |
"""
edad = int(input("Ingrese su edad: "))
if 0 <= edad <= 12:
    print("Niño")
elif 13 <= edad <= 17:
    print("Adolescente")
elif 18 <= edad <= 59:
    print("Adulto")
else:
    print("Adulto mayor")

"""
4. Verificar hora del día

Descripción: Pedir la hora (0 a 23) e indicar si es mañana, tarde o noche.

"""
hora = int(input("Ingrese la hora (0-23): "))
if 0 <= hora < 12:
    print("Mañana")
elif 12 <= hora < 18:
    print("Tarde")
else:
    print("Noche")