export default class CL_Vendedor{
    constructor(codigo, sueldo, montVendido){
        this.codigo = codigo;
        this.sueldo = sueldo;
        this.montVendido = montVendido;
    }

    set codigo(codigo){
        this._codigo = codigo;
    }

    get codigo(){
        return this._codigo ;
    }

    set sueldo(sueldo){
        this._sueldo = +sueldo;
    }

    get sueldo(){
        return this._sueldo ;
    }
    
    set montVendido(montVendido){
        this._montVendido = +montVendido;
    }

    get montVendido(){
        return this._montVendido ;
    }

    sueldoFinal(){
        return this.sueldo + (this.montVendido * 0.25)
    }
}