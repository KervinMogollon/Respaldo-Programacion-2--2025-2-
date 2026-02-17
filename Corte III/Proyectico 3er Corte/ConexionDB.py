import psycopg2

class ConexionDB:
    def __init__(self):
        self.conn = None
        
    def conectar(self):
        if self.conn is None or self.conn.closed:
            self.conn = psycopg2.connect(
                host="localhost",
                database="Proyectos",
                user="postgres",
                password="181201",
                port="5432"
            )

    def cerrar(self):
        if self.conn:
            try:
                self.conn.close()
            except Exception:
                pass
            
    def mostrarTareas(self):
        self.conectar()
        cursor = self.conn.cursor() # type: ignore
        try:
            query = "SELECT * FROM tareas_desarrollo where status = 'A' ORDER BY id_tarea"
            cursor.execute(query)
            result = cursor.fetchall()
            self.conn.commit() # type: ignore
            return result
        finally:
            cursor.close()
            
    def mostrarTareasFiltradas(self, estado=None, asignado=None):
        self.conectar()
        cursor = self.conn.cursor() # type: ignore
        try:
            # Siempre filtramos por Status='A' (Activos)
            query = "SELECT * FROM tareas_desarrollo WHERE status = 'A'"
            params = []

            if estado and estado != "Todos":
                query += " AND estado = %s"
                params.append(estado)
            
            if asignado and asignado.strip() != "":
                query += " AND asignado_a = %s"
                params.append(asignado)

            cursor.execute(query, tuple(params))
            return cursor.fetchall()
        finally:
            cursor.close()

    def _execute_fetchone(self, query, params=()):
        self.conectar()
        cur = self.conn.cursor() # type: ignore
        try:
            cur.execute(query, params)
            res = cur.fetchone()
            self.conn.commit() # type: ignore
            return res
        finally:
            cur.close()

    def _execute(self, query, params=()):
        self.conectar()
        cur = self.conn.cursor() # type: ignore
        try:
            cur.execute(query, params)
            self.conn.commit() # type: ignore
        finally:
            cur.close()
        
    def buscarTareaDB(self, Id_Tarea):
        return self._execute_fetchone("SELECT * FROM tareas_desarrollo WHERE id_tarea = %s", (Id_Tarea,))

    def reactivarTareaDB(self, Id_Tarea):
        self._execute("UPDATE tareas_desarrollo SET status = %s WHERE id_tarea = %s", ('A', Id_Tarea))

    def agregarTareaDB(self, tarea):
        self._execute(
            "INSERT INTO tareas_desarrollo VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (tarea.Id_Tarea, tarea.Titulo, tarea.Descripcion, tarea.Prioridad, tarea.Estado, tarea.Asignado_a, tarea.Fecha_Creacion, tarea.Fecha_Finalizacion, tarea.status)
        )

    def modificarTareaDB(self, Tareas_Desarrollo):
        self._execute(
            "UPDATE tareas_desarrollo\
                SET\
                    titulo = %s,\
                    descripcion = %s,\
                    prioridad = %s,\
                    estado = %s,\
                    asignado_a = %s,\
                    fecha_creacion = %s,\
                    fecha_finalizacion = %s\
                WHERE id_tarea = %s",
            (Tareas_Desarrollo.Titulo,
             Tareas_Desarrollo.Descripcion,
             Tareas_Desarrollo.Prioridad,
             Tareas_Desarrollo.Estado,
             Tareas_Desarrollo.Asignado_a,
             Tareas_Desarrollo.Fecha_Creacion,
             Tareas_Desarrollo.Fecha_Finalizacion,
             Tareas_Desarrollo.Id_Tarea)
        )
        
    def eliminarTareaDB(self, Id_Tarea):
        self._execute("UPDATE tareas_desarrollo SET status = %s WHERE id_tarea = %s", ('I', Id_Tarea))
        
    def EliminarTareasDBSiDone(self, Id_Tarea):
        self._execute("DELETE FROM tareas_desarrollo WHERE id_tarea = %s and estado = %s", (Id_Tarea, 'Done'))