# ConexionDB.py (versión recomendada)
import psycopg2

class ConexionDB:
    def __init__(self):
        self.conn = None

    def conectar(self):
        if self.conn is None or self.conn.closed:
            self.conn = psycopg2.connect(
                host="localhost",
                database="ventas",
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

    def buscarDB(self, idVendedor):
        return self._execute_fetchone("SELECT * FROM vendedore WHERE vendid = %s", (idVendedor,))

    def reactivar(self, idVendedor):
        self._execute("UPDATE vendedore SET status = %s WHERE vendid = %s", ('A', idVendedor))

    def agregarDB(self, vendedor):
        self._execute(
            "INSERT INTO vendedore (vendid, nombrecompleto, ciudad, comision, status) VALUES (%s, %s, %s, %s, %s)",
            (vendedor.vendId, vendedor.nombreCompleto, vendedor.ciudad, vendedor.comision, vendedor.status)
        )

    def modificarDB(self, vendedor):
        self._execute(
            "UPDATE vendedore SET nombrecompleto = %s, ciudad = %s, comision = %s WHERE vendid = %s",
            (vendedor.nombreCompleto, vendedor.ciudad, vendedor.comision, vendedor.vendId)
        )

    def eliminarDB(self, idVendedor):
        self._execute("UPDATE vendedore SET status = %s WHERE vendid = %s", ('I', idVendedor))

    
    
        


"""
cursor = conn.cursor()

cursor.execute('Select * from vendedore')
rows = cursor.fetchall()

for item in rows:
    print("-" * 70)
    print(item)

print("-" * 70)"""