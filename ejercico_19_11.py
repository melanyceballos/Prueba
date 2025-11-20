#modulo 2- clase 19/11/2025
from dataclasses import dataclass

@dataclass
class Producto_Industrial:
    _nombre: str
    _categoria: str
    _codigo_interno: str
    _precio_unitario: float
    _cantidad_inventario: int
    
    @property
    def nombre(self) -> str:
        return self._nombre
    @nombre.setter
    def nombre(self, valor: str) -> None:
        if isinstance(valor,str) and valor.strip():
            self._nombre = valor
        else:
            raise ValueError("El nombre debe de ser un texto valido")
        
    @property
    def categoria(self) -> str:
        return self._categoria
    
    @categoria.setter
    def categoria(self, valor: str) -> None:
        if isinstance(valor,str) and valor.strip():
            self._categoria = valor
        else:
            raise ValueError("La categoria debe de ser un texto valido")
    
    @property
    def codigo_interno(self) -> str:
        return self._codigo_interno
    
    @codigo_interno.setter
    def codigo_interno(self, valor: str) -> None:
        if isinstance(valor,str) and valor.strip():
            self._codigo_interno = valor
        else:
            raise ValueError("El codigo interno debe de ser un texto valido")
        
    @property
    def precio_unitario(self) -> float:
        return self._precio_unitario
    
    @precio_unitario.setter
    def precio_unitario(self, valor: float) -> None:
        if isinstance(valor,float) and valor > 0 :
            self._precio_unitario = valor
        else:
            raise ValueError("El precio unitario debe ser un numero entero o decimal")
    
    @property
    def cantidad_inventario(self) -> int:
        return self._cantidad_inventario
    
    @cantidad_inventario.setter
    def cantidad_inventario(self, valor: int) -> None:
        if isinstance(valor,int) and valor > 0 :
            self._cantidad_inventario = valor
        else:
            raise ValueError("La cantidad del inventario debe ser un numero entero")
        
    def __repr__(self) -> str:
        return(
            f"Producto_Industrial(nombre='{self._nombre}, categoria='{self._categoria}',codigo_interno'{self._codigo_interno}, precio_unitario='{self._precio_unitario}',cantidad_inventario='{self._cantidad_inventario}',"
            
        )
def main() ->None:
    producto_Industrial = Producto_Industrial("lija", "herramienta", "123-456", 100000.00, 11)
    
    print("\n*Informacion del producto*")

    producto_Industrial.nombre = "lija"
    producto_Industrial.cantidad_inventario = 11
    
    print("*Datos del producto*")
    print(producto_Industrial)
    
    print("<<Programa finalizado>>")
if __name__ == "__main__":
    main()