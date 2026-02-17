import tkinter as tk
from tkinter import messagebox

from ConexionDB import ConexionDB


class Aplication:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tareas")
        self.window.geometry("400x320")
        
        #Area de Botones
        
        self.buttonBuscar = tk.Button(self.window, text='Buscar', command=self.BuscarTarea)
        self.buttonBuscar.place(x=20, y=15)
        
        self.buttonEliminar = tk.Button(self.window, text='Eliminar', command=self.EliminarTarea)
        self.buttonEliminar.place(x=80, y=15)
        
        #Area de Entrys
        #Correcion: agregar label y entry para el nuevo atributo titulo
        #tambien se modifico la posicion de los demas labels y entrys para dar espacio al nuevo campo
        self.labelInterfazTareas = tk.Label(self.window, text='Menu de Tareas')
        self.labelInterfazTareas.place(x=20, y=60)
        #Correcion: modificar el tamaño del los entry
        self.labelID = tk.Label(self.window, text='ID:')
        self.labelID.place(x=20 ,y=90)
        self.entryID = tk.Entry(self.window)
        self.entryID.place(x=25 ,y=110)
        self.entryID.config(width=5)
        
        self.labelTitulo = tk.Label(self.window, text='Titulo:')
        self.labelTitulo.place(x=20 ,y=130)
        self.entryTitulo = tk.Entry(self.window)
        self.entryTitulo.place(x=25 ,y=150)
        self.entryTitulo.config(width=30)
        
        self.labelDescripcion = tk.Label(self.window, text='Descripcion:')
        self.labelDescripcion.place(x=20 ,y=170)
        self.entryDescripcion = tk.Entry(self.window)
        self.entryDescripcion.place(x=25 ,y=190)
        self.entryDescripcion.config(width=50)
        
        self.labelCantidadHoras = tk.Label(self.window, text='Cantidad de Horas:')
        self.labelCantidadHoras.place(x=20 ,y=210)
        self.entryCantidadHoras = tk.Entry(self.window)
        self.entryCantidadHoras.place(x=25 ,y=230)
        self.entryCantidadHoras.config(width=5)
        
        
        self.window.mainloop()
    #Correccion: agregar el entryTitulo para limpiar el nuevo campo
    def limpiarEntrys(self):
        self.entryID.delete(0, tk.END) 
        self.entryTitulo.delete(0, tk.END)
        self.entryDescripcion.delete(0, tk.END)
        self.entryCantidadHoras.delete(0, tk.END)   
        
    #Correccion: agregar entryTitulo.insert para porder agregar el atributo faltante
    #tambien se corrigio la nueva posicion de estatus a resultado[4], que se desplazo por la agreacion de la columna titulo
    #tambien se desplazaron los indices en las demas lineas correspondientes
    def BuscarTarea(self):
        idT = self.entryID.get()
        
        if not idT:
            messagebox.showwarning("Advertencia", "Por favor ingrese un ID en el espacio de ID.")
            return
        
        conexion = ConexionDB()
        resultado = conexion.buscarDB(idT)
        conexion.cerrar()
        
        if resultado:
            self.limpiarEntrys()
            if resultado[4] == 'A':
                self.entryID.insert(0, idT)
                self.entryTitulo.insert(0, resultado[1])
                self.entryDescripcion.insert(0, resultado[2])
                self.entryCantidadHoras.insert(0, str(resultado[3]))
                
            elif resultado[4] == 'I':
                activacion = messagebox.askyesno("Información", "La tarea está inactivo. ¿Quieres activarla?")
                if activacion:
                    try:
                        conexion = ConexionDB()
                        conexion.reactivar(idT)
                        messagebox.showinfo("Información", "Tarea reactivada correctamente.")
                        # limpiar campos o actualizar vista
                        self.limpiarEntrys()
                        self.entryID.insert(0, idT)
                        self.entryTitulo.insert(0, resultado[1])
                        self.entryDescripcion.insert(0, resultado[2])
                        self.entryCantidadHoras.insert(0, str(resultado[3]))
                    except Exception as e:
                        messagebox.showerror("Error", f"No se pudo reactivar la tarea: {e}")
                else:
                    # Usuario respondió No (False)
                    messagebox.showinfo("Información", "la tarea sigue inactiva.")
                    self.limpiarEntrys()
        else:
            messagebox.showinfo("Información", "tarea no encontrada.")
    #Correccion: Al igual que en BuscarTarea, se corrigio el indice de estatus a resultado[4] por la gracion de la columna titulo
    def EliminarTarea(self):
        idT = self.entryID.get()
        
        if not idT:
            messagebox.showwarning("Advertencia", "Por favor ingrese un ID de tarea.")
            return

        conexion = ConexionDB()
        resultado = conexion.buscarDB(idT)
        conexion.cerrar()
        if resultado[4] == 'I': # type: ignore
            messagebox.showinfo("Información", "la tarea ya está Eliminada.")
            return
        elif resultado[4] == 'A': # type: ignore
            try:
                conexion = ConexionDB()
                conexion.eliminarDB(idT)
                messagebox.showinfo("Información", "tarea eliminada correctamente.")
                self.limpiarEntrys()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo eliminar la tarea: {e}")
        else:
            messagebox.showinfo("Información", "tarea no encontrada.")