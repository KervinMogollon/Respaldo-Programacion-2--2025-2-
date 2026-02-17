import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter import Toplevel, BOTH, END
import datetime as dt

from ConexionDB import ConexionDB
from Cl_Student import Student


class Wd_Students:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Estudiantes")
        self.window.geometry("400x400")
        
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
            command=self.BuscarEstudiante
            ).place(x=20, y=35)
        
        #boton agregar
        self.buttonAgregar = tk.Button(
            self.window, 
            text='Agregar', 
            command=self.agregarEstudiante
            ).place(x=80, y=35)
        
        #boton modificar
        self.buttonModificar = tk.Button(
            self.window, text='Modificar', command=self.modificarEstudiante
            ).place(x=140, y=35)
        
        #boton eliminar
        self.buttonEliminar = tk.Button(
            self.window, 
            text='Eliminar', 
            command=self.eliminarEstudiante
            ).place(x=210, y=35)
        
        #boton limpiar los entrys
        self.buttonLimpiar = tk.Button(
            self.window, 
            text='Limpiar', 
            command=self.limpiarEntrys
            ).place(x=280, y=35)
        
        # Etiqueta y campo de texto para CI del estudiante
        self.labelCi = tk.Label(
            self.window, 
            text='CI Estudiante:'
            ).place(x=20, y=70)
        self.entryCi = tk.Entry(self.window)
        self.entryCi.place(x=140, y=70)
        
        # Etiqueta y campo de texto para nombre del estudiante
        self.labelNombre = tk.Label(
            self.window, 
            text='Nombre Estudiante:'
            ).place(x=20, y=100)
        self.entryNombre = tk.Entry(self.window)
        self.entryNombre.place(x=140, y=100)

        # Etiqueta y campo de texto para dirección del estudiante
        self.labelDireccion = tk.Label(
            self.window, 
            text='Dirección Estudiante:'
            ).place(x=20, y=130)
        self.entryDireccion = tk.Entry(self.window)
        self.entryDireccion.place(x=140, y=130)
        
        self.labelTelefono = tk.Label(
            self.window, 
            text='Teléfono Estudiante:'
            ).place(x=20, y=160)
        self.entryTelefono = tk.Entry(self.window)
        self.entryTelefono.place(x=140, y=160)
        
        self.labelFechaNacimiento = tk.Label(
            self.window, 
            text='Fecha Nacimiento:'
            ).place(x=20, y=190)
        self.entryFechaNacimiento = tk.Entry(self.window)
        self.entryFechaNacimiento.place(x=140, y=190)
        
        self.labelFechaIngreso = tk.Label(
            self.window, 
            text='Fecha Registro:'
            ).place(x=20, y=220)
        self.entryFechaIngreso = tk.Entry(self.window)
        self.entryFechaIngreso.place(x=140, y=220)
        
        self.labelCarrera = tk.Label(
            self.window, 
            text='Carrera:'
            ).place(x=20, y=250)
        self.entryCarrera = tk.Entry(self.window)
        self.entryCarrera.place(x=140, y=250)
        
        #Mostrar todos los estudiantes de la base de datos
        self.buttonMostrar = tk.Button(
            self.window,
            text='Mostrar Estudiantes', 
            command=self.mostrarEstudiantes
            ).place(x=20, y=290)
        
        #boton para volver al menu principal
        self.buttonVolverMenu = tk.Button(
            self.window,
            text='Volver al Menú Principal',
            command=self.volverMenu
            ).place(x=200, y=290)
        
        
        self.window.mainloop()
    
    def volverMenu(self):
        from AppWd_Menu import Wd_Menu
        self.window.destroy()
        app_menu = Wd_Menu()
        
    def limpiarEntrys(self):
        self.entryCi.delete(0, tk.END)
        self.entryNombre.delete(0, tk.END)
        self.entryDireccion.delete(0, tk.END)
        self.entryTelefono.delete(0, tk.END)
        self.entryFechaNacimiento.delete(0, tk.END)
        self.entryFechaIngreso.delete(0, tk.END)
        self.entryCarrera.delete(0, tk.END)
        
    #funcion para mostrar toda la iformacion de todos los estudiantes en la base de datos
    def mostrarEstudiantes(self):
        conexion = ConexionDB()
        resultado = conexion.mostrarStudentsDB()
        conexion.cerrar()

        if not resultado:
            messagebox.showinfo("Estudiantes", "No hay estudiantes para mostrar.")
            return

        texto = []
        texto.append("Estudiantes Activos:\n")
        for estudiante in resultado:
            if estudiante[7] == 'A':
                texto.append(
                    f"CI: {estudiante[0]}\nNombre: {estudiante[1]}\nDirección: {estudiante[2]}\n"
                    f"Teléfono: {estudiante[3]}\nFecha Nacimiento: {estudiante[4]}\n"
                    f"Fecha Registro: {estudiante[5]}\nCarrera: {estudiante[6]}\n"
                )

        texto.append("\nEstudiantes Inactivos:\n")
        for estudiante in resultado:
            if estudiante[7] == 'I':
                texto.append(
                    f"CI: {estudiante[0]}\nNombre: {estudiante[1]}\nDirección: {estudiante[2]}\n"
                    f"Teléfono: {estudiante[3]}\nFecha Nacimiento: {estudiante[4]}\n"
                    f"Fecha Registro: {estudiante[5]}\nCarrera: {estudiante[6]}\n"
                )

        contenido = "\n".join(texto)

        top = Toplevel(self.window)
        top.title("Estudiantes")
        top.geometry("700x500")          # ajusta a tu preferencia
        st = ScrolledText(top, wrap='word')
        st.pack(fill=BOTH, expand=True)
        st.insert(END, contenido)
        st.configure(state='disabled')

    
    def ExisteDB(self, ciStudent):
        conexion = ConexionDB()
        result = conexion.buscarStudentDB(ciStudent)
        if result:
            conexion.cerrar()
            return True
        else:
            conexion.cerrar()
            return False
        
    def BuscarEstudiante(self):
        ciStudent = self.entryCi.get()
        if not ciStudent:
            messagebox.showwarning("Advertencia", "Por favor ingrese una CI de estudiante.")
            return
            
        
        conexion = ConexionDB()
        try:
            resultado = conexion.buscarStudentDB(ciStudent)
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al buscar el estudiante: {e}")
            return
        finally:
            conexion.cerrar()
        
        if resultado:
            self.limpiarEntrys()
            if resultado[7] == 'A':
                #preparar entryTelefono por si acaso es nulo en la base de datos
                if resultado[3] is None:
                    resultado = list(resultado)
                    resultado[3] = ""
                self.entryCi.insert(0, ciStudent)
                self.entryNombre.insert(0, resultado[1])
                self.entryDireccion.insert(0, resultado[2])
                self.entryTelefono.insert(0, resultado[3])
                self.entryFechaNacimiento.insert(0, resultado[4])
                self.entryFechaIngreso.insert(0, resultado[5])
                self.entryCarrera.insert(0, resultado[6])
            elif resultado[7] == 'I':
                activacion = messagebox.askyesno("Información", "El estudiante está inactivo, ¿Quiere reactivarlo?")
                if activacion:
                    try:
                        #preparar entryTelefono por si acaso es nulo en la base de datos
                        if resultado[3] is None:
                            resultado = list(resultado)
                            resultado[3] = ""
                        conexion = ConexionDB()
                        conexion.reactivarStudent(ciStudent)
                        messagebox.showinfo("Información", "Estudiante reactivado exitosamente.")
                        self.limpiarEntrys()
                        self.entryCi.insert(0, ciStudent)
                        self.entryNombre.insert(0, resultado[1])
                        self.entryDireccion.insert(0, resultado[2])
                        self.entryTelefono.insert(0, resultado[3])
                        self.entryFechaNacimiento.insert(0, resultado[4])
                        self.entryFechaIngreso.insert(0, resultado[5])
                        self.entryCarrera.insert(0, resultado[6])
                    except Exception as e:
                        messagebox.showerror("Error", f"Ocurrió un error al reactivar el estudiante: {e}")
                    finally:
                        conexion.cerrar()
                else:
                    messagebox.showinfo("Información", "El estudiante permanece inactivo.")
        else:
            messagebox.showinfo("Información", "Estudiante no encontrado en la base de datos.")
    
    def agregarEstudiante(self):
        idS = self.entryCi.get()
        nombreS = self.entryNombre.get()
        direccionS = self.entryDireccion.get()
        telefonoS = self.entryTelefono.get() #este no es un campo obligatorio
        fechaNacimientoS = self.entryFechaNacimiento.get()
        fechaIngresoS = self.entryFechaIngreso.get()
        carreraS = self.entryCarrera.get()
        
        if not idS or not nombreS or not direccionS or not fechaNacimientoS or not fechaIngresoS or not carreraS:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos Requeridos.")
            return
        
        if self.ExisteDB(idS):
            messagebox.showwarning("Advertencia", "Ya Existe un estudiante con este CI.")
            return
        
        #Hacer que las fechas sean del tipo datetime
        try:
            fechaNacimientoS = dt.datetime.strptime(fechaNacimientoS, "%Y-%m-%d")
            fechaIngresoS = dt.datetime.strptime(fechaIngresoS, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha incorrecto. Use AAAA-MM-DD.")
            return
        
        nuevoEstudiante = Student()
        nuevoEstudiante.StudCi = idS
        nuevoEstudiante.StudName = nombreS
        nuevoEstudiante.StudAddress = direccionS
        nuevoEstudiante.StudPhone = telefonoS
        nuevoEstudiante.StudBirthDate = fechaNacimientoS
        nuevoEstudiante.StudRegisteredDate = fechaIngresoS
        nuevoEstudiante.StudCareer = carreraS
        try:
            conexion = ConexionDB()
            conexion.agregarStudentDB(nuevoEstudiante)
            conexion.cerrar()
            messagebox.showinfo("Información", "Estudiante agregado exitosamente.")
            self.limpiarEntrys()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al agregar el estudiante: {e}")
    
    def modificarEstudiante(self):
        ciS = self.entryCi.get()
        nombreS = self.entryNombre.get()
        direccionS = self.entryDireccion.get()
        telefonoS = self.entryTelefono.get() #este no es un campo obligatorio
        fechaNacimientoS = self.entryFechaNacimiento.get()
        fechaIngresoS = self.entryFechaIngreso.get()
        carreraS = self.entryCarrera.get()
        
        if not ciS or not nombreS or not direccionS or not fechaNacimientoS or not fechaIngresoS or not carreraS:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos Requeridos.")
            return
        
        if not self.ExisteDB(ciS):
            messagebox.showwarning("Advertencia", "No existe un estudiante con este CI.")
            return
        
        #Hacer que las fechas sean del tipo datetime
        try:
            fechaNacimientoS = dt.datetime.strptime(fechaNacimientoS, "%Y-%m-%d")
            fechaIngresoS = dt.datetime.strptime(fechaIngresoS, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Formato de fecha incorrecto. Use AAAA-MM-DD.")
            return
        
        estudianteModificado = Student()
        estudianteModificado.StudCi = ciS
        estudianteModificado.StudName = nombreS
        estudianteModificado.StudAddress = direccionS
        estudianteModificado.StudPhone = telefonoS
        estudianteModificado.StudBirthDate = fechaNacimientoS
        estudianteModificado.StudRegisteredDate = fechaIngresoS
        estudianteModificado.StudCareer = carreraS
        
        try:
            conexion = ConexionDB()
            conexion.modificarStudentDB(estudianteModificado)
            conexion.cerrar()
            messagebox.showinfo("Información", "Estudiante modificado exitosamente.")
            self.limpiarEntrys()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al modificar el estudiante: {e}")
    
    def eliminarEstudiante(self):
        ciS = self.entryCi.get()
        
        if not ciS:
            messagebox.showwarning("Advertencia", "Por favor ingrese el CI del estudiante a eliminar.")
            return
        
        if not self.ExisteDB(ciS):
            messagebox.showwarning("Advertencia", "No existe un estudiante con este CI.")
            return
        
        try:
            conexion = ConexionDB()
            conexion.eliminarStudentDB(ciS)
            conexion.cerrar()
            messagebox.showinfo("Información", "Estudiante eliminado exitosamente.")
            self.limpiarEntrys()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al eliminar el estudiante: {e}")