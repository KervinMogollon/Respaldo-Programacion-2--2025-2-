# Cl_vendedor.py
class Vendedor:
    def __init__(self, codigo: str, sueldo: float, monto_vendido: float):
        self.codigo = codigo
        self.sueldo = float(sueldo)
        self.monto_vendido = float(monto_vendido)

    def sueldo_final(self) -> float:
        return self.sueldo + (self.monto_vendido * 0.25)
