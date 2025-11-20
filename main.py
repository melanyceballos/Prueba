#modulo 2- clase 17/11/2025
# Operadores Relaconales

variableX = 5
variableY = 10

variableZ, VariableW = 8, 7

print(f"variableX == variableY: {variableX == variableY}:")
print(f"variableZ != VariableX: {variableZ != variableX}: ") 
print(f"VariableY > variableW: {variableY > VariableW}: ")
print(f"variableX < variableZ: {variableX < variableZ}: ")
print(f"VariableW >= variabley: {VariableW >= variableY}: ")
print(f"variableZ <= variableW: {variableZ <= VariableW}: ")

## Operadores Logicos
## and, or, not
## and: Devuelve True si ambas condiciones son verdaderas
## and = si tengo el viernes AND tengo dinero = True
## or: Devuelve True si al menos una de las condiciones es verdadera
## or = si tengo el viernes OR tengo dinero = True
## not: Invierte el valor de verdad de una condicion

tiene_dinero = True
esta_libre = False

print(f"AND: {tiene_dinero and esta_libre}: ")
print(f"OR: {tiene_dinero or esta_libre}: ")
print(f"NOT: {not esta_libre}: ")


##ejercicio

edad = 1
nombre = "Mimi"
especie = "gato"

print(f"edad: {edad}, nombre: {nombre}, especie: {especie}")

## ejercicio 2

edad = input("Ingresa tu edad: ")

## input() -> caracter
## isdigit() -> devuelve True si todos los caracteres son digitos
## int(input()) -> convierte el valor de input a entero
## float(input()) -> convierte el valor de input a flotante

if edad.isdigit():
    edad = int(edad)
    print(f"La edad es valida: {edad}")
else:
    print("La edad no es valida")
    
tiene_dinero = False
if tiene_dinero:
    print("Salgamos este viernes")
else:
    print("Te deseo exitos ")
    
## ejercicio 3

esta_lloviendo = True
esta_cargado_el_celular = True
estoy_enferma = False

if esta_lloviendo:
    print("Es mejor no salir")
else:
    print("Se puede salir sin problemas")
    
if esta_cargado_el_celular:
    print("Se puede usar")
else:
    print("Ponlo a cargar")
        

if estoy_enferma:
    print(":D")
else:
    print("Toma medicamento y descansa D:")
    
""" 
OPERADORES RELACIONALES

Enunciado:
Crea un programa en Python que pida al usuario ingresar dos números
 muestre en pantalla el resultado de las siguientes comparaciones:

Si el primer número es mayor que el segundo.

Si el primer número es menor que el segundo.

Si ambos números son iguales.

"""
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

if numero1 > numero2:
    print(f"El primer numero es mayor que el segundo numero: {numero1 > numero2}: ")

if numero1 < numero2:
    print(f"El primer numero es menor que el segundo numero: {numero1 < numero2}: ")
    
if numero1 == numero2:
    print(f"Ambos numeros son iguales: {numero1 == numero2}: ")


    
17

"""
EJERCICIOS

Ejercicio 1: Verificar mayoría de edad
1. Enunciado:
Pide la edad de una persona y muestra un mensaje si es mayor de edad (18 años o más).

2. Ejercicio 2: Determinar si un número es positivo
Enunciado:
Pide un número y muestra un mensaje si el número es positivo.

3. Ejercicio 3: Verificar rango de valores

Enunciado:
Pide un número y muestra un mensaje solo si está entre 10 y 50 (inclusive).
"""
#  1: Verificar mayoría de edad
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
    
#  2: Determinar si un número es positivo
numero = int(input("Ingresa un número: "))
if numero > 0:
    print("El número es positivo.") 
else:
    print("El número es negativo.")

#  3: Verificar rango de valores
valor = int(input("Ingresa un número: "))   
if 10 <= valor <= 50:
    print("El número está entre 10 y 50.")
else:
    print("El número está fuera del rango de 10 a 50.")
    