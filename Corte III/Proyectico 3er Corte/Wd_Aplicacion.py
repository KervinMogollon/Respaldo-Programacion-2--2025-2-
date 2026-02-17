import tkinter as tk
from tkinter import ttk

from ConexionDB import ConexionDB

class Aplicacion:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tareas")
        self.window.geometry("1000x400") # Aumenté el ancho para ver mejor las columnas
        
        # Botón para ir a la ventana de gestión
        self.buttonGestionDB = tk.Button(
            self.window, 
            text='Gestión de Tareas', 
            command=self.abrirGestionDB
        )
        self.buttonGestionDB.place(x=15, y=15)
        
        # En el __init__ de Aplicacion
        self.labelFiltroEstado = tk.Label(self.window, text="Estado:").place(x=150, y=10)
        self.comboFiltroEstado = ttk.Combobox(self.window, values=["Todos", "To Do", "In Progress", "Testing", "Done"])
        self.comboFiltroEstado.current(0)
        self.comboFiltroEstado.place(x=200, y=10, width=100)

        self.labelFiltroPersona = tk.Label(self.window, text="Asignado:").place(x=310, y=10)
        self.entryFiltroPersona = tk.Entry(self.window)
        self.entryFiltroPersona.place(x=370, y=10, width=100)

        self.btnFiltrar = tk.Button(self.window, text="Filtrar", command=self.aplicar_filtro).place(x=480, y=7)
        
        # Llamamos a la creación de la tabla
        self.MostrarTodasTareas()
        
        self.window.mainloop()

    def abrirGestionDB(self):
        from Wd_GestionDB import GestionDB
        self.window.destroy()
        self.newWindow = GestionDB()

    def ordenar_columna(self, col, reverse):
        # 1. Obtener todos los elementos de la tabla
        # .set(k, col) obtiene el valor de la fila k en la columna col
        lista_datos = [(self.tabla.set(k, col), k) for k in self.tabla.get_children('')]

        # 2. Ordenar la lista (Python detecta si es número o texto)
        lista_datos.sort(reverse=reverse)

        # 3. Reorganizar los elementos en la interfaz según el nuevo orden
        for index, (val, k) in enumerate(lista_datos):
            self.tabla.move(k, '', index)

        # 4. Cambiar el comando del encabezado para que la próxima vez sea inverso
        self.tabla.heading(col, command=lambda: self.ordenar_columna(col, not reverse))

    def MostrarTodasTareas(self):
        conexion = ConexionDB()
        tareas = conexion.mostrarTareas()
        
        columns = ["Id_Tarea", "Titulo", "Descripcion", "Prioridad", "Estado", "Asignado_a", "Fecha_Creacion", "Fecha_Finalizacion"]
        
        # Guardamos la tabla en 'self.tabla' para que otros métodos puedan acceder a ella
        self.tabla = ttk.Treeview(self.window, columns=columns, show='headings')
        
        self.tabla.bind("<<TreeviewSelect>>", self.seleccionar_fila)
        # Configurar cada columna
        for col in columns:
            # Aquí está el truco: añadimos el command para ordenar
            self.tabla.heading(
                col, 
                text=col, 
                command=lambda _col=col: self.ordenar_columna(_col, False)
            )
            # Ajustamos un ancho estándar
            self.tabla.column(col, width=100)
        
        # Insertar los datos
        for tarea in tareas:
            self.tabla.insert("", "end", values=tarea)
        
        self.tabla.pack(pady=70, padx=10, fill='both', expand=True)
    
    def aplicar_filtro(self):
        estado = self.comboFiltroEstado.get()
        persona = self.entryFiltroPersona.get()
        
        # Llamamos a la base de datos con los parámetros
        conexion = ConexionDB()
        tareas = conexion.mostrarTareasFiltradas(estado, persona)
        
        # Limpiamos el Treeview
        for item in self.tabla.get_children():
            self.tabla.delete(item)
            
        # Llenamos con los resultados filtrados
        for tarea in tareas:
            self.tabla.insert("", "end", values=tarea)
        
    def seleccionar_fila(self, event):
        # 1. Obtener el ID de la fila seleccionada
        item_seleccionado = self.tabla.focus()
        if not item_seleccionado:
            return

        # 2. Obtener los valores de esa fila
        valores = self.tabla.item(item_seleccionado, 'values')

        # 3. Abrir la ventana de gestión pasando estos valores
        self.abrirGestionDB_con_datos(valores)
        self.window.destroy()
        
    def abrirGestionDB_con_datos(self, datos):
        from Wd_GestionDB import GestionDB
        # Creamos la ventana de gestión
        ventana_gestion = GestionDB()
        # Llamamos a un método interno de esa ventana para cargar los datos
        ventana_gestion.cargar_datos_en_formulario(datos)
        