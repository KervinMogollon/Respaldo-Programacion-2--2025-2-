class Tarea:
    def __init__(self):
        self.Id: str
        #Correccion: agregando el atributo titulo faltante
        self.titulo: str
        self.descripcion: str
        self.CantidadHoras: int
        #Correccion: Cambiando el atributo status a estatus
        self.estatus = 'A'