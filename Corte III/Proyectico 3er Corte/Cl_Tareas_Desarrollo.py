import datetime as dt

class Tarea_Desarrollo:
    def __init__(self):
        self.Id_Tarea: str
        self.Titulo: str
        self.Descripcion: str
        self.Prioridad: str
        self.Estado: str
        self.Asignado_a: str
        self.Fecha_Creacion: dt.datetime
        self.Fecha_Finalizacion: dt.datetime
        self.status = 'A'