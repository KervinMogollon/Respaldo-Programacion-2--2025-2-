import tkinter as tk
from tkinter import messagebox

class Wd_Menu:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Menú de Inscripciones")
        self.window.geometry("300x200")
        
            # Botón para abrir la ventana de estudiantes
        self.buttonEstudiantes = tk.Button(self.window, text='Gestión de Estudiantes', command=self.abrirEstudiantes)
        self.buttonEstudiantes.place(x=70, y=50)
        
        # Botón para salir de la aplicación
        self.buttonSalir = tk.Button(self.window, text='Salir', command=self.window.quit)
        self.buttonSalir.place(x=120, y=100)
               
        self.window.mainloop()
    
    def abrirEstudiantes(self):
        from AppWd_Students import Wd_Students
        self.window.destroy()
        app_students = Wd_Students()