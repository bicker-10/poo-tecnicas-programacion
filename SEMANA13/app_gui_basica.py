import tkinter as tk
from tkinter import messagebox


class AplicacionGUI:
    """
    Clase principal de la aplicación.
    Se encarga de crear la interfaz gráfica y manejar los eventos.
    """

    def __init__(self, root):
        """
        Constructor de la clase.
        Recibe la ventana principal y configura todos los componentes.
        """
        self.root = root
        self.root.title("Aplicación GUI Básica - Registro de Datos")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # -------------------------------
        # TÍTULO PRINCIPAL
        # -------------------------------
        self.label_titulo = tk.Label(
            root,
            text="Registro de Datos con Tkinter",
            font=("Arial", 16, "bold")
        )
        self.label_titulo.pack(pady=10)

        # -------------------------------
        # MARCO PARA ENTRADA DE DATOS
        # -------------------------------
        self.frame_entrada = tk.Frame(root)
        self.frame_entrada.pack(pady=10)

        self.label_dato = tk.Label(
            self.frame_entrada,
            text="Ingrese un dato:",
            font=("Arial", 11)
        )
        self.label_dato.grid(row=0, column=0, padx=5, pady=5)

        self.entry_dato = tk.Entry(self.frame_entrada, width=30, font=("Arial", 11))
        self.entry_dato.grid(row=0, column=1, padx=5, pady=5)

        # Permite agregar datos presionando Enter
        self.entry_dato.bind("<Return>", self.agregar_dato_evento)

        # -------------------------------
        # MARCO PARA BOTONES
        # -------------------------------
        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(pady=10)

        self.boton_agregar = tk.Button(
            self.frame_botones,
            text="Agregar",
            width=15,
            command=self.agregar_dato
        )
        self.boton_agregar.grid(row=0, column=0, padx=5, pady=5)

        self.boton_limpiar_entrada = tk.Button(
            self.frame_botones,
            text="Limpiar entrada",
            width=15,
            command=self.limpiar_entrada
        )
        self.boton_limpiar_entrada.grid(row=0, column=1, padx=5, pady=5)

        self.boton_limpiar_seleccion = tk.Button(
            self.frame_botones,
            text="Limpiar selección",
            width=15,
            command=self.limpiar_seleccion
        )
        self.boton_limpiar_seleccion.grid(row=0, column=2, padx=5, pady=5)

        # -------------------------------
        # ETIQUETA PARA LA LISTA
        # -------------------------------
        self.label_lista = tk.Label(
            root,
            text="Datos registrados:",
            font=("Arial", 11)
        )
        self.label_lista.pack(pady=5)

        # -------------------------------
        # MARCO PARA LISTA Y SCROLLBAR
        # -------------------------------
        self.frame_lista = tk.Frame(root)
        self.frame_lista.pack(pady=10)

        self.scrollbar = tk.Scrollbar(self.frame_lista, orient=tk.VERTICAL)

        self.listbox_datos = tk.Listbox(
            self.frame_lista,
            width=50,
            height=10,
            font=("Arial", 11),
            yscrollcommand=self.scrollbar.set
        )
        self.listbox_datos.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar.config(command=self.listbox_datos.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # -------------------------------
        # ETIQUETA INFORMATIVA
        # -------------------------------
        self.label_info = tk.Label(
            root,
            text="Seleccione un elemento de la lista para poder eliminarlo.",
            font=("Arial", 9),
            fg="gray"
        )
        self.label_info.pack(pady=5)

    def agregar_dato(self):
        """
        Agrega el texto ingresado en el Entry al Listbox.
        Valida que no esté vacío antes de agregarlo.
        """
        dato = self.entry_dato.get().strip()

        if dato == "":
            messagebox.showwarning("Campo vacío", "Por favor, ingrese un dato antes de agregar.")
            return

        self.listbox_datos.insert(tk.END, dato)
        self.entry_dato.delete(0, tk.END)
        self.entry_dato.focus()

    def agregar_dato_evento(self, event):
        """
        Variante del método agregar_dato para ser usada con el evento Enter.
        """
        self.agregar_dato()

    def limpiar_entrada(self):
        """
        Limpia el contenido del campo de texto.
        """
        self.entry_dato.delete(0, tk.END)
        self.entry_dato.focus()

    def limpiar_seleccion(self):
        """
        Elimina el elemento seleccionado en la lista.
        Si no hay ningún elemento seleccionado, muestra una advertencia.
        """
        seleccion = self.listbox_datos.curselection()

        if not seleccion:
            messagebox.showwarning(
                "Sin selección",
                "Seleccione un elemento de la lista para eliminarlo."
            )
            return

        self.listbox_datos.delete(seleccion[0])


# -------------------------------
# PUNTO DE ENTRADA DEL PROGRAMA
# -------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionGUI(root)
    root.mainloop()