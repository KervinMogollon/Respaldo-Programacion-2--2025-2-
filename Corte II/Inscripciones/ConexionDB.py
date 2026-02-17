import psycopg2

class ConexionDB:
    def __init__(self):
        self.conn = None
        
    def conectar(self):
        if self.conn is None or self.conn.closed:
            self.conn = psycopg2.connect(
                host="localhost",
                database="Inscripciones",
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
            
    def mostrarStudentsDB(self):
        self.conectar()
        cursor = self.conn.cursor() # type: ignore
        try:
            query = "SELECT * FROM estudiantes"
            cursor.execute(query)
            result = cursor.fetchall()
            self.conn.commit() # type: ignore
            return result
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
        
    def buscarStudentDB(self, ciStudent):
        return self._execute_fetchone("SELECT * FROM estudiantes WHERE ci = %s", (ciStudent,))
    
    def reactivarStudent(self, ciStudent):
        self._execute("UPDATE estudiantes SET status = %s WHERE ci = %s", ('A', ciStudent))
    
    def agregarStudentDB(self, student):
        self._execute(
            "INSERT INTO estudiantes VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (student.StudCi, student.StudName, student.StudAddress, student.StudPhone, student.StudBirthDate, student.StudRegisteredDate, student.StudCareer, student.status)
        )
    
    def modificarStudentDB(self, student):
        self._execute(
            "UPDATE estudiantes\
                SET\
                    nombre = %s,\
                    direccion = %s,\
                    nrotelefono = %s,\
                    fechanacimiento = %s,\
                    fechaInscripcion = %s,\
                    carrera = %s,\
                    status = %s\
                WHERE ci = %s",
            (student.StudName, 
             student.StudAddress, 
             student.StudPhone, 
             student.StudBirthDate, 
             student.StudRegisteredDate, 
             student.StudCareer, 
             student.status,
             student.StudCi)
        )
        
    def eliminarStudentDB(self, ciStudent):
        self._execute("UPDATE estudiantes SET status = %s WHERE ci = %s", ('I', ciStudent))