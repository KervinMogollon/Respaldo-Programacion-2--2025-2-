export class Concurso {
    constructor(){
        this.aspirantes = [];
    }
    agregarAspirante(aspirante) {
        this.aspirantes.push(aspirante);
    }
    /*
    3.1. concurso.apruebanCon(nota) : aspirante[]
	      + nota: la mínima aprobatoria
		  + retorna un array con los datos de quienes aprueban el concurso
    */

    apruebanCon(nota) {
        return this.aspirantes.filter(a => a.puntaje >= nota);
        
    }
}