# principal.py
from Cl_Vendedor import Vendedor
from Cl_Zapateria import Zapateria

def main():
    # 1. Crear los vendedores
    vend1 = Vendedor("V001", 150, 4000)
    vend2 = Vendedor("V002", 130, 2000)
    vend3 = Vendedor("V003", 140, 4750)
    vend4 = Vendedor("V004", 155, 3850)

    # 2. Crear la zapatería y procesar ventas
    zap = Zapateria()
    for v in (vend1, vend2, vend3, vend4):
        zap.procesar_vendedor(v)

    # 3. Imprimir resultados
    print(f"Sueldo obtenido por el {vend1.codigo} es de {vend1.sueldo_final():.2f} BsF")
    print(f"Sueldo obtenido por el {vend2.codigo} es de {vend2.sueldo_final():.2f} BsF")
    print(f"Sueldo obtenido por el {vend3.codigo} es de {vend3.sueldo_final():.2f} BsF")
    print(f"Sueldo obtenido por el {vend4.codigo} es de {vend4.sueldo_final():.2f} BsF\n")

    print(f"Promedio de ventas = {zap.promedio_ventas():.2f} BsF")
    print(f"Mayor venta realizada fue {zap.venta_mayor():.2f} BsF")

if __name__ == "__main__":
    main()
