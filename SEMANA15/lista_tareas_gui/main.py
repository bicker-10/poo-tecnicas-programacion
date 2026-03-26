import tkinter as tk
from tkinter import messagebox


class AplicacionListaTareas:
    def __init__(self, root):
        """
        Constructor de la aplicación.
        Aquí se configuran la ventana principal, los widgets
        y los eventos necesarios para el funcionamiento.
        """
        self.root = root
        self.root.title("Aplicación GUI de Lista de Tareas")
        self.root.geometry("550x450")
        self.root.resizable(False, False)

        # Lista interna para almacenar las tareas y su estado
        # Cada tarea será un diccionario con:
        # {"texto": "Estudiar POO", "completada": False}
        self.tareas = []

        # Título principal
        self.label_titulo = tk.Label(
            root,
            text="Gestor de Lista de Tareas",
            font=("Arial", 16, "bold")
        )
        self.label_titulo.pack(pady=10)

        # Frame para entrada de texto
        self.frame_entrada = tk.Frame(root)
        self.frame_entrada.pack(pady=10)

        self.label_tarea = tk.Label(self.frame_entrada, text="Nueva tarea:")
        self.label_tarea.grid(row=0, column=0, padx=5)

        self.entry_tarea = tk.Entry(self.frame_entrada, width=35, font=("Arial", 12))
        self.entry_tarea.grid(row=0, column=1, padx=5)

        # Evento: presionar Enter para añadir tarea
        self.entry_tarea.bind("<Return>", self.agregar_tarea_evento)

        # Botón añadir tarea
        self.boton_agregar = tk.Button(
            self.frame_entrada,
            text="Añadir Tarea",
            command=self.agregar_tarea,
            width=15,
            bg="#4CAF50",
            fg="white"
        )
        self.boton_agregar.grid(row=0, column=2, padx=5)

        # Frame para lista de tareas
        self.frame_lista = tk.Frame(root)
        self.frame_lista.pack(pady=10)

        self.listbox_tareas = tk.Listbox(
            self.frame_lista,
            width=60,
            height=15,
            font=("Arial", 11),
            selectbackground="#a6a6a6"
        )
        self.listbox_tareas.pack(side=tk.LEFT)

        # Barra de desplazamiento
        self.scrollbar = tk.Scrollbar(self.frame_lista, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox_tareas.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox_tareas.yview)

        # Evento opcional: doble clic para marcar como completada
        self.listbox_tareas.bind("<Double-Button-1>", self.marcar_completada_evento)

        # Frame para botones inferiores
        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(pady=15)

        self.boton_completar = tk.Button(
            self.frame_botones,
            text="Marcar como Completada",
            command=self.marcar_completada,
            width=22,
            bg="#2196F3",
            fg="white"
        )
        self.boton_completar.grid(row=0, column=0, padx=10)

        self.boton_eliminar = tk.Button(
            self.frame_botones,
            text="Eliminar Tarea",
            command=self.eliminar_tarea,
            width=18,
            bg="#f44336",
            fg="white"
        )
        self.boton_eliminar.grid(row=0, column=1, padx=10)

        # Evento adicional: tecla Delete para eliminar tarea seleccionada
        self.root.bind("<Delete>", self.eliminar_tarea_evento)

    def agregar_tarea(self):
        """
        Añade una nueva tarea a la lista si el campo de entrada no está vacío.
        """
        texto_tarea = self.entry_tarea.get().strip()

        if texto_tarea == "":
            messagebox.showwarning("Campo vacío", "Por favor, escribe una tarea.")
            return

        nueva_tarea = {"texto": texto_tarea, "completada": False}
        self.tareas.append(nueva_tarea)

        self.actualizar_listbox()

        # Limpiar el campo de entrada después de agregar
        self.entry_tarea.delete(0, tk.END)
        self.entry_tarea.focus()

    def agregar_tarea_evento(self, event):
        """
        Manejador de evento para la tecla Enter en el Entry.
        """
        self.agregar_tarea()

    def marcar_completada(self):
        """
        Marca la tarea seleccionada como completada.
        Si ya está completada, no la vuelve a cambiar.
        """
        seleccion = self.listbox_tareas.curselection()

        if not seleccion:
            messagebox.showwarning("Sin selección", "Selecciona una tarea para marcarla.")
            return

        indice = seleccion[0]

        if self.tareas[indice]["completada"]:
            messagebox.showinfo("Información", "La tarea ya está marcada como completada.")
            return

        self.tareas[indice]["completada"] = True
        self.actualizar_listbox()

    def marcar_completada_evento(self, event):
        """
        Manejador de evento para doble clic sobre una tarea.
        """
        self.marcar_completada()

    def eliminar_tarea(self):
        """
        Elimina la tarea seleccionada de la lista.
        """
        seleccion = self.listbox_tareas.curselection()

        if not seleccion:
            messagebox.showwarning("Sin selección", "Selecciona una tarea para eliminarla.")
            return

        indice = seleccion[0]
        del self.tareas[indice]

        self.actualizar_listbox()

    def eliminar_tarea_evento(self, event):
        """
        Manejador de evento para eliminar una tarea usando la tecla Delete.
        """
        self.eliminar_tarea()

    def actualizar_listbox(self):
        """
        Actualiza visualmente la lista de tareas en el Listbox.
        Las tareas completadas mostrarán un indicador especial.
        """
        self.listbox_tareas.delete(0, tk.END)

        for tarea in self.tareas:
            if tarea["completada"]:
                texto_mostrado = f"✔ {tarea['texto']} (Completada)"
            else:
                texto_mostrado = f"✘ {tarea['texto']}"

            self.listbox_tareas.insert(tk.END, texto_mostrado)


# Bloque principal de ejecución
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionListaTareas(root)
    root.mainloop()