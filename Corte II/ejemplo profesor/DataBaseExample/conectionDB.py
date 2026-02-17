import psycopg2

class ConectionDB:

    def __init__(self):
        self.conn = psycopg2.connect(
            host =  'localhost',
            database = 'postgres',
            user = 'postgres',
            password = 'XtremePostgreSQL#13',
            port = '5432'
        )
    
    def searchDB(self,id):
        self.cursor = self.conn.cursor()
        sql = 'SELECT * FROM products where product_id=%s;'
        self.cursor.execute(sql,(id,))
        row = self.cursor.fetchone()
        self.disconnect()
        return row
    
    def reactivate(self, id):
        self.cursor = self.conn.cursor()
        sql = 'update products set status=%s where product_id=%s;'
        self.cursor.execute(sql,('A',id,))
        self.disconnect()
        
    def disconnect(self):
        self.conn.close()
        self.cursor.close()
    