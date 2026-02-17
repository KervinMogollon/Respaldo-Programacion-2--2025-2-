/**
 * CALZADOS MILDRED
Calzados “Mildred” establece las siguientes políticas para sus vendedores: un sueldo base y
cada vendedor tendrá una comisión del 25% sobre el monto vendido. De cada empleado se sabe:
su código y monto vendido. Se requiere un programa que muestre por Vendedor: Sueldo Obtenido
y por la Zapatería: b) Promedio de Ventas y la mayor venta realizada.
Sueldo obtenido por el V001 es 1150
Sueldo obtenido por el V002 es 630
Sueldo obtenido por el V003 es 1327.50
Sueldo obtenido por el V003 es 1117.50
Promedio de ventas 3650
Mayor venta realizada 4750
La salida corresponde a los siguientes datos del vendedor (código del vendedor y monto
vendido)
(V001,150, 4000) (V002,130,2000) (V003,140,4750) (V004,155,3850)
 */

import CL_Zapateria from "./Zapateria.js";
import CL_Vendedor from "./Vendedor.js";

let vend1 = new CL_Vendedor("V001", 150, 4000),
    vend2 = new CL_Vendedor("V002", 130, 2000),
    vend3 = new CL_Vendedor("V003", 140, 4750),
    vend4 = new CL_Vendedor("V004", 155, 3850);

let zap = new CL_Zapateria();

zap.procesarVendedor(vend1);
zap.procesarVendedor(vend2);
zap.procesarVendedor(vend3);
zap.procesarVendedor(vend4);

let salida = document.getElementById("salida")

salida.innerHTML = `
<br>Sueldo obtenido por el ${vend1.codigo} es de ${(vend1.sueldoFinal()).toFixed(2)} BsF
<br>Sueldo obtenido por el ${vend2.codigo} es de ${(vend2.sueldoFinal()).toFixed(2)} BsF
<br>Sueldo obtenido por el ${vend3.codigo} es de ${(vend3.sueldoFinal()).toFixed(2)} BsF
<br>Sueldo obtenido por el ${vend4.codigo} es de ${(vend4.sueldoFinal()).toFixed(2)} BsF
<br>
<br>Promedio de ventas = ${(zap.promdVentas()).toFixed(2)} BsF
<br>Mayor venta realizada fue ${(zap.ventaMayor()).toFixed(2)} BsF
`