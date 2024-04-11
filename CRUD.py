import tkinter as tk
from tkinter import PhotoImage

class Interfaz:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Marcador Financiero: Ingresos y Gastos")
        self.ventana.geometry("1200x400")

        # Cargar la imagen de fondo
        self.imagen_fondo = PhotoImage(file="fondo.png")

        # Crear un canvas del tamaño de la ventana
        self.canvas = tk.Canvas(ventana, width=1200, height=400)
        self.canvas.pack(fill="both", expand=True)

        # Colocar la imagen de fondo en el canvas
        self.canvas.create_image(0, 0, image=self.imagen_fondo, anchor="nw")

        self.frame_entradas = tk.Frame(self.canvas, bg="", padx=20, pady=20)
        self.frame_entradas.grid(row=0, column=0, padx=20, pady=20, sticky="n")

        self.frame_lista = tk.Frame(self.canvas, bg="", padx=20, pady=20)
        self.frame_lista.grid(row=0, column=1, padx=20, pady=20, sticky="n")

        self.etiqueta_numero = tk.Label(self.frame_entradas, text="N°:", font=("Helvetica", 14), bg="#f0f0f0")
        self.etiqueta_numero.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.entry_numero = tk.Entry(self.frame_entradas, font=("Helvetica", 12))
        self.entry_numero.grid(row=0, column=1, padx=10, pady=10)

        self.etiqueta_tipo = tk.Label(self.frame_entradas, text="Tipo:", font=("Helvetica", 14), bg="#f0f0f0")
        self.etiqueta_tipo.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.tipo_var = tk.StringVar(self.frame_entradas)
        self.tipo_var.set("Ingreso")
        self.opciones_tipo = ["Ingreso", "Gasto"]
        self.entry_tipo = tk.OptionMenu(self.frame_entradas, self.tipo_var, *self.opciones_tipo)
        self.entry_tipo.config(font=("Helvetica", 12), bg="#f0f0f0", width=15)
        self.entry_tipo.grid(row=1, column=1, padx=10, pady=10)

        self.etiqueta_categoria = tk.Label(self.frame_entradas, text="Categoria:", font=("Helvetica", 14), bg="#f0f0f0")
        self.etiqueta_categoria.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.categoria_var = tk.StringVar(self.frame_entradas)
        self.categoria_var.set("Transporte")
        self.opciones_categoria = ["Transporte", "Alimentación", "Servicios", "Inversión"]
        self.entry_categoria = tk.OptionMenu(self.frame_entradas, self.categoria_var, *self.opciones_categoria)
        self.entry_categoria.config(font=("Helvetica", 12), bg="#f0f0f0", width=15)
        self.entry_categoria.grid(row=2, column=1, padx=10, pady=10)

        self.etiqueta_descripcion = tk.Label(self.frame_entradas, text="Descripción:", font=("Helvetica", 14), bg="#f0f0f0")
        self.etiqueta_descripcion.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.entry_descripcion = tk.Entry(self.frame_entradas, font=("Helvetica", 12))
        self.entry_descripcion.grid(row=3, column=1, padx=10, pady=10)

        self.etiqueta_valor = tk.Label(self.frame_entradas, text="Valor:", font=("Helvetica", 14), bg="#f0f0f0")
        self.etiqueta_valor.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.entry_valor = tk.Entry(self.frame_entradas, font=("Helvetica", 12))
        self.entry_valor.grid(row=4, column=1, padx=10, pady=10)

        self.boton_agregar = tk.Button(self.frame_entradas, text="Agregar", font=("Helvetica", 14), command=self.agregar_lista)
        self.boton_agregar.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

        self.boton_listar = tk.Button(self.frame_entradas, text="Listar", font=("Helvetica", 14), command=self.listar_info)
        self.boton_listar.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

        self.boton_limpiar = tk.Button(self.frame_entradas, text="Limpiar", font=("Helvetica", 14), command=self.limpiar_lista)
        self.boton_limpiar.grid(row=5, column=2, padx=10, pady=10, sticky="ew")

        self.titulos = ["N°", "Tipo", "Categoria", "Descripción", "Valor"]
        self.lista = []

    def agregar_lista(self):
        numero = self.entry_numero.get()
        tipo = self.tipo_var.get()
        categoria = self.categoria_var.get()
        descripcion = self.entry_descripcion.get()
        valor = self.entry_valor.get()

        self.lista.append((numero, tipo, categoria, descripcion, valor))

        self.entry_numero.delete(0, tk.END)
        self.entry_descripcion.delete(0, tk.END)
        self.entry_valor.delete(0, tk.END)

    def listar_info(self):
        # Limpiar la lista antes de mostrar los nuevos valores
        self.frame_lista.destroy()
        self.frame_lista = tk.Frame(self.canvas, bg="", padx=20, pady=20)
        self.frame_lista.grid(row=0, column=1, padx=20, pady=20, sticky="n")

        # Mostrar los titulos
        for i, titulo in enumerate(self.titulos):
            tk.Label(self.frame_lista, text=titulo, font=("Helvetica", 14, "bold"), bg="#f0f0f0").grid(row=0, column=i, padx=10, pady=10)

        # Mostrar los datos de la lista
        for i, persona in enumerate(self.lista):
            for j, dato in enumerate(persona):
                tk.Label(self.frame_lista, text=dato, font=("Helvetica", 12), bg="#f0f0f0").grid(row=i+1, column=j, padx=10, pady=10)

    def limpiar_lista(self):
        # Limpiar la lista
        self.lista = []

        # Limpiar la lista en la interfaz
        self.frame_lista.destroy()
        self.frame_lista = tk.Frame(self.canvas, bg="", padx=20, pady=20)
        self.frame_lista.grid(row=0, column=1, padx=20, pady=20, sticky="n")

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = Interfaz(ventana_principal)
    ventana_principal.mainloop()
