from ConexionDB import ConexionDB as DB

class ContexDbStudent:
    def __init__(self):
        self.Db = DB()
        
    
    def buscarStudentDB(self, ciStudent):
        return self.Db._execute_fetchone("SELECT * FROM estudiantes WHERE ci = %s", (ciStudent,))
    
    def reactivarStudent(self, ciStudent):
        self.Db._execute("UPDATE estudiantes SET status = %s WHERE ci = %s", ('A', ciStudent))
    
    def agregarStudentDB(self, student):
        self.Db._execute(
            "INSERT INTO estudiantes VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (student.StudCi, student.StudName, student.StudAddress, student.StudPhone, student.StudBirthDate, student.StudRegisteredDate, student.StudCareer, student.status)
        )
    
    def modificarStudentDB(self, student):
        self.Db._execute(
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
        self.Db._execute("UPDATE estudiantes SET status = %s WHERE ci = %s", ('I', ciStudent))