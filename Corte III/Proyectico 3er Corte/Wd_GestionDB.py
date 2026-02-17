import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

import datetime as dt

from ConexionDB import ConexionDB
from Cl_Tareas_Desarrollo import Tarea_Desarrollo


class GestionDB:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("gestión de Tareas")
        self.window.geometry("320x550")
        
        #Aqui empezamos a construir elementos de la ventana
        
        #areas de botones
        self.labelButtons = tk.Label(
            self.window, 
            text='Área de Botones'
            ).place(x=20, y=10)
        
        #boton buscar
        self.buttonBuscar = tk.Button(
            self.window, 
            text='Buscar', 
            command=self.BuscarTarea
            ).place(x=20, y=35)
        
        #boton agregar
        self.buttonAgregar = tk.Button(
            self.window, 
            text='Agregar', 
            command=self.agregarTarea
            ).place(x=70, y=35)
        
        #boton modificar
        self.buttonModificar = tk.Button(
            self.window, text='Modificar', command=self.modificarTarea
            ).place(x=125, y=35)
        
        #boton eliminar
        self.buttonEliminar = tk.Button(
            self.window, 
            text='Eliminar', 
            command=self.eliminarTarea
            ).place(x=190, y=35)
        
        #boton limpiar los entrys
        self.buttonLimpiar = tk.Button(
            self.window, 
            text='Limpiar', 
            command=self.limpiarEntrys
            ).place(x=245, y=35)
        
        #Etiqueta y entry para Id_Tarea
        self.labelId_Tarea = tk.Label(
            self.window, 
            text='Id Tarea:'
            ).place(x=20, y=75)
        self.entryId_Tarea = tk.Entry(self.window)
        self.entryId_Tarea.place(x=30, y=100)
      
        #Etiqueta y entry para Titulo
        self.labelTitulo = tk.Label(
            self.window, 
            text='Título:'
            ).place(x=20, y=125)
        self.entryTitulo = tk.Entry(self.window)
        self.entryTitulo.place(x=30, y=150)
        
        #Etiqueta y entry para Descripcion
        self.labelDescripcion = tk.Label(
            self.window, 
            text='Descripción:'
            ).place(x=20, y=175)
        self.entryDescripcion = tk.Entry(self.window)
        self.entryDescripcion.place(x=30, y=200)
        
        #Etiqueta y entry para Prioridad
        self.labelPrioridad = tk.Label(
            self.window, 
            text='Prioridad:'
            ).place(x=20, y=225)
        self.entryPrioridad = ttk.Combobox(self.window, values=["Alta", "Media", "Baja"])
        self.entryPrioridad.place(x=30, y=250)

        #Etiqueta y entry para Estado
        self.labelEstado = tk.Label(
            self.window, 
            text='Estado:'
            ).place(x=20, y=275)
        self.entryEstado = ttk.Combobox(self.window, values=["To Do", "In Progress", "Testing", "Done"])
        self.entryEstado.place(x=30, y=300)

        #Etiqueta y entry para Asignado_a
        self.labelAsignado_a = tk.Label(
            self.window, 
            text='Asignado a:'
            ).place(x=20, y=325)
        self.entryAsignado_a = tk.Entry(self.window)
        self.entryAsignado_a.place(x=30, y=350)

        #Etiqueta y entry para Fecha_Creacion
        self.labelFecha_Creacion = tk.Label(
            self.window, 
            text='Fecha Creación:'
            ).place(x=20, y=375)
        self.entryFecha_Creacion = tk.Entry(self.window)
        self.entryFecha_Creacion.place(x=30, y=400)
        
        #Etiqueta y entry para Fecha_Finalizacion
        self.labelFecha_Finalizacion = tk.Label(
            self.window, 
            text='Fecha Finalización:'
            ).place(x=20, y=425)
        self.entryFecha_Finalizacion = tk.Entry(self.window)
        self.entryFecha_Finalizacion.place(x=30, y=450)
        
        self.buttonVolver = tk.Button(
            self.window, 
            text='Volver al Menu Principal', 
            command=self.volverAplicacion
            ).place(x=15, y=500)
        
        self.buttonEliminarDone = tk.Button(
            self.window, 
            text='Eliminar si Done', 
            command=self.EliminarTareasSiDone
            ).place(x=180, y=500)

        
    
    def volverAplicacion(self):
        from Wd_Aplicacion import Aplicacion
        self.window.destroy()
        self.newWindow = Aplicacion()
        
    def limpiarEntrys(self):
        self.entryId_Tarea.delete(0, tk.END)
        self.entryTitulo.delete(0, tk.END)
        self.entryDescripcion.delete(0, tk.END)
        self.entryPrioridad.delete(0, tk.END)
        self.entryEstado.delete(0, tk.END)
        self.entryAsignado_a.delete(0, tk.END)
        self.entryFecha_Creacion.delete(0, tk.END)
        self.entryFecha_Finalizacion.delete(0, tk.END)

    def ExisteDB(self, Id_Tarea):
        conexion = ConexionDB()
        result = conexion.buscarTareaDB(Id_Tarea)
        if result:
            conexion.cerrar()
            return True
        else:
            conexion.cerrar()
            return False
    
    def BuscarTarea(self):
        Id_Tarea = self.entryId_Tarea.get()
        
        if not Id_Tarea:
            messagebox.showwarning("Advertencia", "Por favor ingrese un ID de tarea.")
            return
            
        
        conexion = ConexionDB()
        try:
            resultado = conexion.buscarTareaDB(Id_Tarea)
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al buscar la tarea: {e}")
            return
        finally:
            conexion.cerrar()
        
        if resultado:
            self.limpiarEntrys()
            if resultado[8] == 'A':
                #preparar entryTelefono por si acaso es nulo en la base de datos
                if resultado[7] is None:
                    resultado = list(resultado)
                    resultado[7] = ""
                self.entryId_Tarea.insert(0, Id_Tarea)
                self.entryTitulo.insert(0, resultado[1])
                self.entryDescripcion.insert(0, resultado[2])
                self.entryPrioridad.insert(0, resultado[3])
                self.entryEstado.insert(0, resultado[4])
                self.entryAsignado_a.insert(0, resultado[5])
                self.entryFecha_Creacion.insert(0, resultado[6])
                self.entryFecha_Finalizacion.insert(0, resultado[7])
            elif resultado[8] == 'I':
                activacion = messagebox.askyesno("Información", "La Tarea está inactiva, ¿Quiere reactivarla?")
                if activacion:
                    try:
                        #preparar entryTelefono por si acaso es nulo en la base de datos
                        if resultado[3] is None:
                            resultado = list(resultado)
                            resultado[3] = ""
                        conexion = ConexionDB()
                        conexion.reactivarTareaDB(Id_Tarea)
                        messagebox.showinfo("Información", "Tarea reactivada exitosamente.")
                        self.limpiarEntrys()
                        self.entryId_Tarea.insert(0, Id_Tarea)
                        self.entryTitulo.insert(0, resultado[1])
                        self.entryDescripcion.insert(0, resultado[2])
                        self.entryPrioridad.insert(0, resultado[3])
                        self.entryEstado.insert(0, resultado[4])
                        self.entryAsignado_a.insert(0, resultado[5])
                        self.entryFecha_Creacion.insert(0, resultado[6])
                        self.entryFecha_Finalizacion.insert(0, resultado[7])
                    except Exception as e:
                        messagebox.showerror("Error", f"Ocurrió un error al reactivar la tarea: {e}")
                    finally:
                        conexion.cerrar()
                else:
                    messagebox.showinfo("Información", "La tarea permanece inactiva.")
        else:
            messagebox.showinfo("Información", "Tarea no encontrada en la base de datos.")

    def agregarTarea(self):
        idt = self.entryId_Tarea.get()
        titulo = self.entryTitulo.get()
        descripcion = self.entryDescripcion.get()
        prioridad = self.entryPrioridad.get()
        estado = self.entryEstado.get()
        asignado_a = self.entryAsignado_a.get()
        fecha_creacion = self.entryFecha_Creacion.get()
        fecha_finalizacion = self.entryFecha_Finalizacion.get()
        
        if not idt or not titulo or not descripcion or not prioridad or not estado or not asignado_a or not fecha_creacion:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos Requeridos.")
            return
        
        if self.ExisteDB(idt):
            messagebox.showwarning("Advertencia", "Ya Existe una tarea con este ID.")
            return
        
        #Hacer que las fechas sean del tipo datetime
        try:
            fecha_creacion = dt.datetime.strptime(fecha_creacion, "%Y-%m-%d")
            fecha_finalizacion = dt.datetime.strptime(fecha_finalizacion, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha incorrecto. Use AAAA-MM-DD.")
            return
        
        nuevaTarea = Tarea_Desarrollo()
        nuevaTarea.Id_Tarea = idt
        nuevaTarea.Titulo = titulo
        nuevaTarea.Descripcion = descripcion
        nuevaTarea.Prioridad = prioridad
        nuevaTarea.Estado = estado
        nuevaTarea.Asignado_a = asignado_a
        nuevaTarea.Fecha_Creacion = fecha_creacion
        nuevaTarea.Fecha_Finalizacion = fecha_finalizacion
        try:
            conexion = ConexionDB()
            conexion.agregarTareaDB(nuevaTarea)
            conexion.cerrar()
            messagebox.showinfo("Información", "Tarea agregada exitosamente.")
            self.limpiarEntrys()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al agregar la tarea: {e}")

    def cargar_datos_en_formulario(self, datos):
        # 'datos' es una tupla: (Id, Titulo, Descripcion, Prioridad, Estado, Asignado, FechaC, FechaF)
        
        # Primero limpiamos los campos por si acaso
        self.limpiarEntrys()

        # Insertamos los valores según el índice de la columna en el Treeview
        self.entryId_Tarea.insert(0, datos[0])
        self.entryTitulo.insert(0, datos[1])
        self.entryDescripcion.insert(0, datos[2])
        
        # Para los ComboBox usamos .set()
        self.entryPrioridad.set(datos[3])
        self.entryEstado.set(datos[4])
        
        self.entryAsignado_a.insert(0, datos[5])
        self.entryFecha_Creacion.insert(0, datos[6])
        self.entryFecha_Finalizacion.insert(0, datos[7])
        
        # Opcional: Bloquear el ID para que no se pueda modificar la clave primaria
        self.entryId_Tarea.config(state='readonly')
    
    def modificarTarea(self):
        idt = self.entryId_Tarea.get()
        titulo = self.entryTitulo.get()
        descripcion = self.entryDescripcion.get()
        prioridad = self.entryPrioridad.get()
        estado = self.entryEstado.get()
        asignado_a = self.entryAsignado_a.get()
        fecha_creacion = self.entryFecha_Creacion.get()
        fecha_finalizacion = self.entryFecha_Finalizacion.get()
        
        if not idt or not titulo or not descripcion or not prioridad or not estado or not asignado_a or not fecha_creacion:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos Requeridos.")
            return
        
        if not self.ExisteDB(idt):
            messagebox.showwarning("Advertencia", "No existe una tarea con este ID.")
            return
        
        #Hacer que las fechas sean del tipo datetime
        try:
            fecha_creacion = dt.datetime.strptime(fecha_creacion, "%Y-%m-%d")
            fecha_finalizacion = dt.datetime.strptime(fecha_finalizacion, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha incorrecto. Use AAAA-MM-DD.")
            return
        
        TareaModificada = Tarea_Desarrollo()
        TareaModificada.Id_Tarea = idt
        TareaModificada.Titulo = titulo
        TareaModificada.Descripcion = descripcion
        TareaModificada.Prioridad = prioridad
        TareaModificada.Estado = estado
        TareaModificada.Asignado_a = asignado_a
        TareaModificada.Fecha_Creacion = fecha_creacion
        TareaModificada.Fecha_Finalizacion = fecha_finalizacion
        
        try:
            conexion = ConexionDB()
            conexion.modificarTareaDB(TareaModificada)
            conexion.cerrar()
            messagebox.showinfo("Información", "Tarea modificada exitosamente.")
            self.limpiarEntrys()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al modificar la tarea: {e}")

    def eliminarTarea(self):
        idt = self.entryId_Tarea.get()

        if not idt:
            messagebox.showwarning("Advertencia", "Por favor ingrese un ID de tarea.")
            return

        conexion = ConexionDB()
        resultado = conexion.buscarTareaDB(idt)
        conexion.cerrar()
        if resultado[8] == 'I': # type: ignore
            messagebox.showinfo("Información", "la tarea ya está Eliminada.")
            return
        elif resultado[8] == 'A': # type: ignore
            respuesta = messagebox.askyesno("Confirmación", "¿Está seguro de que desea eliminar esta tarea?")
            if not respuesta:
                return
            elif respuesta:
                try:
                    conexion = ConexionDB()
                    conexion.eliminarTareaDB(idt)
                    messagebox.showinfo("Información", "tarea eliminada correctamente.")
                    self.limpiarEntrys()
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo eliminar la tarea: {e}")
            else:
                messagebox.showinfo("Información", "Operación de eliminación cancelada.")
        else:
            messagebox.showinfo("Información", "tarea no encontrada.")

    def EliminarTareasSiDone(self):
        idt = self.entryId_Tarea.get()
        conexion = ConexionDB()
        
        if not idt:
            messagebox.showwarning("Advertencia", "Por favor ingrese un ID de tarea.")
            return
        
        conexion = ConexionDB()
        resultado = conexion.buscarTareaDB(idt)
        conexion.cerrar()
        
        if resultado:
            if resultado[4] == 'Done': # type: ignore
                respuesta = messagebox.askyesno("Confirmación", "¿Está seguro de que desea eliminar esta tarea permanentemente?")
                if not respuesta:
                    return
                elif respuesta:
                    try:
                        conexion = ConexionDB()
                        conexion.EliminarTareasDBSiDone(idt)
                        messagebox.showinfo("Información", "tarea eliminada permanentemente.")
                        self.limpiarEntrys()
                    except Exception as e:
                        messagebox.showerror("Error", f"No se pudo eliminar la tarea: {e}")
                else:
                    messagebox.showinfo("Información", "Operación de eliminación cancelada.")
            else:
                messagebox.showinfo("Información", "La tarea no está en estado 'Done', no se puede eliminar permanentemente.")
        else:
            messagebox.showinfo("Información", "tarea no encontrada.")