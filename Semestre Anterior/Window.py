import tkinter as tk
import mysql.connector
from Department import Department


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="GracoSoft#00",
    database="test13"
)


class Aplication():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Department Administrator")
        
        self.labelCode = tk.Label(self.window, text="Code:")
        self.labelCode.place(x=100,y=10)
        self.entryCode = tk.Entry(self.window)
        self.entryCode.place(x=140,y=10)

        self.labelDescription = tk.Label(self.window, text="Description:")
        self.labelDescription.place(x=70,y=50)
        self.entryDescription = tk.Entry(self.window)
        self.entryDescription.place(x=140,y=50)

        self.labelNumberEmployees = tk.Label(self.window, text="Number of Employees:")
        self.labelNumberEmployees.place(x=10,y=90)
        self.entryNumberEmployees = tk.Entry(self.window)
        self.entryNumberEmployees.place(x=140,y=90)

        self.buttonClear = tk.Button(self.window, text ="Clear", command=self.Clear)
        self.buttonClear.place(x=140, y=130)

        self.buttonAdd = tk.Button(self.window, text ="Add", command=self.Add)
        self.buttonAdd.place(x=190, y=130)            
    
        self.window.geometry("400x300")
        self.window.mainloop()
    
    def CreateObj(self):
        cod = self.entryCode.get()
        desc = self.entryDescription.get()
        num = int(self.entryNumberEmployees.get())
        objDpto = Department(cod,desc,num)
        return objDpto

    def Add(self):
        obj = self.CreateObj()
        cursor = connection.cursor()
        sql = "INSERT INTO department values(%s,%s,%s,%s)"
        cursor.execute(sql,(obj.code,obj.description,obj.numberEmployees,obj.statusE))
        connection.commit()
        connection.close()
    
    def Clear(self):
        self.entryCode.delete(0,tk.END)
        self.entryDescription.delete(0,tk.END)
        self.entryNumberEmployees.delete(0,tk.END)

def main():
    objAplication = Aplication()

if __name__=="__main__":
    main()