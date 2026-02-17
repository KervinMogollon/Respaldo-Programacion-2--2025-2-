export default class CL_Zapateria{
    constructor(){
        this.vend = 0;
        this.acuVentas = 0;
        this.MayorVenta = 0;
    }

    procesarVendedor(vend){
        this.vend++

        this.acuVentas += vend.montVendido

        if(vend.montVendido > this.MayorVenta)
            this.MayorVenta = vend.montVendido
    }

    promdVentas(){
        return this.acuVentas / this.vend
    }

    ventaMayor(){
        return this.MayorVenta
    }
}