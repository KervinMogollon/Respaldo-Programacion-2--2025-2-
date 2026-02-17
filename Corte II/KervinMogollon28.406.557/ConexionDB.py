import psycopg2

class ConexionDB:
    def __init__(self):
        self.conn = None

    def conectar(self):
        if self.conn is None or self.conn.closed:
            self.conn = psycopg2.connect(
                host="localhost",
                database="TareaDB",
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

    def buscarDB(self, idTarea):
        return self._execute_fetchone("SELECT * FROM tbTarea WHERE idTarea = %s", (idTarea,))

    def reactivar(self, idTarea):
        self._execute("UPDATE tbTarea SET status = %s WHERE idTarea = %s", ('A', idTarea))

    def eliminarDB(self, idTarea):
        self._execute("UPDATE tbTarea SET status = %s WHERE idTarea = %s", ('I', idTarea))