import psycopg2 
class ConexionDB: 
    def __init__(self): 
        self.conn = psycopg2.connect( 
            host="localhost", 
            database="ventas", 
            user="postgres", 
            password="181201", 
            port="5432" ) 
            
    def cerrarConexion(self): 
        self.conn.commit() 
        self.cursor.close() 
        
    def buscarDB(self, idVendedor): 
        self.cursor = self.conn.cursor() 
        query = "SELECT * FROM vendedore WHERE vendid = %s" 
        self.cursor.execute(query, (idVendedor,)) 
        result = self.cursor.fetchone() 
        self.cerrarConexion() 
        return result 
    
    def reactivar(self, idVendedor): 
        self.cursor = self.conn.cursor() 
        query = "UPDATE vendedore SET status = %s WHERE vendid = %s" 
        self.cursor.execute(query, ('A', idVendedor,)) 
        self.cerrarConexion() 
        
    def agregarDB(self, vendedor): 
        self.cursor = self.conn.cursor() 
        query = "INSERT INTO vendedore (vendid, nombrecompleto, ciudad, comision, status) VALUES (%s, %s, %s, %s, %s)" 
        self.cursor.execute(query, (vendedor.vendId, vendedor.nombreCompleto, vendedor.ciudad, vendedor.comision, vendedor.status)) 
        self.cerrarConexion() 
        
    def modificarDB(self, vendedor): 
        self.cursor = self.conn.cursor() 
        query = "UPDATE vendedore SET nombrecompleto = %s, ciudad = %s, comision = %s WHERE vendid = %s" 
        self.cursor.execute(query, (vendedor.nombreCompleto, vendedor.ciudad, vendedor.comision, vendedor.vendId)) 
        self.cerrarConexion() 
        
    def eliminarDB(self, idVendedor): 
        self.cursor = self.conn.cursor() 
        query = "UPDATE vendedore SET status = %s WHERE vendid = %s" 
        self.cursor.execute(query, ('I', idVendedor,)) 
        self.cerrarConexion()