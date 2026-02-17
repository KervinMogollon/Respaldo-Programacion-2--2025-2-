import tkinter as tk
from tkinter import messagebox

from ConexionDB import ConexionDB
from Cl_Vendedor import vendedor

class aplication:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Vendedores")
        self.window.geometry("400x300")
        
        #Aqui empezamos a construir elementos de la ventana
        
        #areas de botones
        self.labelButtons = tk.Label(self.window, text='Área de Botones')
        self.labelButtons.place(x=20, y=10)
        
        #boton buscar
        self.buttonBuscar = tk.Button(self.window, text='Buscar', command=self.BuscarVendedor)
        self.buttonBuscar.place(x=20, y=35)
        
        #boton agregar
        self.buttonAgregar = tk.Button(self.window, text='Agregar', command=self.agregarVendedor)
        self.buttonAgregar.place(x=80, y=35)
        
        #boton modificar
        self.buttonModificar = tk.Button(self.window, text='Modificar', command=self.modificarVendedor)
        self.buttonModificar.place(x=140, y=35)
        
        #boton eliminar
        self.buttonEliminar = tk.Button(self.window, text='Eliminar', command=self.eliminarVendedor)
        self.buttonEliminar.place(x=210, y=35)
        
        #boton limpiar los entrys
        self.buttonLimpiar = tk.Button(self.window, text='Limpiar', command=self.limpiarEntrys)
        self.buttonLimpiar.place(x=280, y=35)
        

        # Etiqueta y campo de texto para ID del vendedor
        self.labelId = tk.Label(self.window, text='ID Vendedor:')
        self.labelId.place(x=20, y=70)
        self.entryId = tk.Entry(self.window)
        self.entryId.place(x=95, y=70)
        
        # Etiqueta y campo de texto para nombre del vendedor
        self.labelNombre = tk.Label(self.window, text='Nombre Vendedor:')
        self.labelNombre.place(x=20, y=100)
        self.entryNombre = tk.Entry(self.window)
        self.entryNombre.place(x=125, y=100)

        # Etiqueta y campo de texto para comisión del vendedor
        self.labelComision = tk.Label(self.window, text='Comisión Vendedor:')
        self.labelComision.place(x=20, y=130)
        self.entryComision = tk.Entry(self.window)
        self.entryComision.place(x=135, y=130)
        
        # Etiqueta y campo de texto para ciudad del vendedor
        self.labelCiudad = tk.Label(self.window, text='Ciudad Vendedor:')
        self.labelCiudad.place(x=20, y=160)
        self.entryCiudad = tk.Entry(self.window)
        self.entryCiudad.place(x=120, y=160)



        self.window.mainloop()#Aqui terminamos de construir elementos de la ventana
    
    def existInDB(self, idVendedor):
        conexion = ConexionDB()
        resultado = conexion.buscarDB(idVendedor)
        conexion.cerrar()
        return resultado is not None
    
    def limpiarEntrys(self):
        self.entryId.delete(0, tk.END)
        self.entryNombre.delete(0, tk.END)
        self.entryComision.delete(0, tk.END)
        self.entryCiudad.delete(0, tk.END)
    
    def BuscarVendedor(self): 
        idVendedor = self.entryId.get()
        if not idVendedor:
            messagebox.showwarning("Advertencia", "Por favor ingrese un ID de vendedor.")
            return
            
        
        conexion = ConexionDB()
        resultado = conexion.buscarDB(idVendedor)
        conexion.cerrar()
        
        if resultado:
            self.limpiarEntrys()
            if resultado[4] == 'A':
                self.entryId.insert(0, idVendedor)
                self.entryNombre.insert(0, resultado[1])
                self.entryCiudad.insert(0, resultado[2])
                self.entryComision.insert(0, str(resultado[3]))
            
            elif resultado[4] == 'I':
                # askyesno devuelve un booleano: True si el usuario responde 'Yes', False si 'No'
                activacion = messagebox.askyesno("Información", "El vendedor está inactivo. ¿Quieres activarlo?")
                if activacion:
                    # Usuario respondió Sí (True)
                    try:
                        conexion = ConexionDB()
                        conexion.reactivar(idVendedor)
                        messagebox.showinfo("Información", "Vendedor reactivado correctamente.")
                        # limpiar campos o actualizar vista
                        self.limpiarEntrys()
                        self.entryId.insert(0, idVendedor)
                        self.entryNombre.insert(0, resultado[1])
                        self.entryCiudad.insert(0, resultado[2])
                        self.entryComision.insert(0, str(resultado[3]))
                    except Exception as e:
                        messagebox.showerror("Error", f"No se pudo reactivar el vendedor: {e}")
                else:
                    # Usuario respondió No (False)
                    messagebox.showinfo("Información", "El vendedor sigue inactivo.")
                    self.limpiarEntrys()
            
        else:
            messagebox.showinfo("Información", "Vendedor no encontrado.")
    
    def agregarVendedor(self):
        idVendedor = self.entryId.get()
        nombreVendedor = self.entryNombre.get()
        ciudadVendedor = self.entryCiudad.get()
        comisionVendedor = self.entryComision.get()
        
        if not idVendedor or not nombreVendedor or not ciudadVendedor or not comisionVendedor:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")
            return
        
        if self.existInDB(idVendedor):
            messagebox.showwarning("Advertencia", "El ID del vendedor ya existe en la base de datos.")
            return
        
        try:
            comisionVendedor = float(comisionVendedor)
        except ValueError:
            messagebox.showerror("Error", "La comisión debe ser un número válido.")
            return
        
        nuevoVendedor = vendedor()
        nuevoVendedor.vendId = idVendedor
        nuevoVendedor.nombreCompleto = nombreVendedor
        nuevoVendedor.ciudad = ciudadVendedor
        nuevoVendedor.comision = comisionVendedor
        nuevoVendedor.status = 'A'
        
        try:
            conexion = ConexionDB()
            conexion.agregarDB(nuevoVendedor)
            messagebox.showinfo("Información", "Vendedor agregado correctamente.")
            self.limpiarEntrys()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo agregar el vendedor: {e}")   
    
    def modificarVendedor(self):
        idVendedor = self.entryId.get()
        nombreVendedor = self.entryNombre.get()
        ciudadVendedor = self.entryCiudad.get()
        comisionVendedor = self.entryComision.get()
        
        if not idVendedor or not nombreVendedor or not ciudadVendedor or not comisionVendedor:
            messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")
            return
        
        if not self.existInDB(idVendedor):
            messagebox.showwarning("Advertencia", "El ID del vendedor no existe en la base de datos.")
            return
        
        try:
            comisionVendedor = float(comisionVendedor)
        except ValueError:
            messagebox.showerror("Error", "La comisión debe ser un número válido.")
            return
        
        vendedorModificado = vendedor()
        vendedorModificado.vendId = idVendedor
        vendedorModificado.nombreCompleto = nombreVendedor
        vendedorModificado.ciudad = ciudadVendedor
        vendedorModificado.comision = comisionVendedor
        vendedorModificado.status = 'A'
        
        try:
            conexion = ConexionDB()
            conexion.modificarDB(vendedorModificado)
            messagebox.showinfo("Información", "Vendedor modificado correctamente.")
            self.limpiarEntrys()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo modificar el vendedor: {e}")
            
    def eliminarVendedor(self):
        idVendedor = self.entryId.get()
        
        if not idVendedor:
            messagebox.showwarning("Advertencia", "Por favor ingrese un ID de vendedor.")
            return
        
        if not self.existInDB(idVendedor):
            messagebox.showwarning("Advertencia", "El ID del vendedor no existe en la base de datos.")
            return
        
        #ya se verificó que el vendedor existe en la base de datos
        #ahora verifiquemos si el status es 'I' o 'A'
        conexion = ConexionDB()
        resultado = conexion.buscarDB(idVendedor)
        conexion.cerrar()
        if resultado[4] == 'I': # type: ignore
            messagebox.showinfo("Información", "El vendedor ya está Eliminado.")
            return
        
        try:
            conexion = ConexionDB()
            conexion.eliminarDB(idVendedor)
            messagebox.showinfo("Información", "Vendedor eliminado correctamente.")
            self.limpiarEntrys()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar el vendedor: {e}")        