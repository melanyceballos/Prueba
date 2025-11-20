def saludar():
    print("Hola parce... (pana)")
def saludo():
    return "Hola parce... (pana)"
print (saludo())

## funciones con parametros
def saludotres(nombre):
    print(f"como estas? {nombre}")
saludotres("Melany Ceballos")
saludotres(3)

def suma(numerouno: int, numerodos:int) -> int:
    resultado = numerouno + numerodos
    print(f"El resultado de la suma es: {resultado}")
suma(8,10)
##