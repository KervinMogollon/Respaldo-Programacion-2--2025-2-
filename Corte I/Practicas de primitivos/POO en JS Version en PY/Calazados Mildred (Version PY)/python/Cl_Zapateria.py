# Cl_zapateria.py
class Zapateria:
    def __init__(self):
        self.num_vendedores = 0
        self.acu_ventas = 0.0
        self.mayor_venta = 0.0

    def procesar_vendedor(self, vend):
        self.num_vendedores += 1

        self.acu_ventas += vend.monto_vendido
        
        if vend.monto_vendido > self.mayor_venta:
            self.mayor_venta = vend.monto_vendido

    def promedio_ventas(self) -> float:
        if self.num_vendedores == 0:
            return 0.0
        return self.acu_ventas / self.num_vendedores

    def venta_mayor(self) -> float:
        return self.mayor_venta
