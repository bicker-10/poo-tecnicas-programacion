import tkinter as tk
from tkinter import messagebox


class AplicacionTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("500x450")
        self.root.resizable(False, False)

        # Lista donde se almacenan las tareas
        # Cada tarea será un diccionario con texto y estado de completado
        self.tareas = []

        # -----------------------------
        # TÍTULO
        # -----------------------------
        self.label_titulo = tk.Label(
            root,
            text="Aplicación GUI para Gestión de Tareas",
            font=("Arial", 14, "bold")
        )
        self.label_titulo.pack(pady=10)

        # -----------------------------
        # FRAME DE ENTRADA
        # -----------------------------
        self.frame_entrada = tk.Frame(root)
        self.frame_entrada.pack(pady=10)

        self.entry_tarea = tk.Entry(self.frame_entrada, width=35, font=("Arial", 12))
        self.entry_tarea.grid(row=0, column=0, padx=5)

        self.btn_agregar = tk.Button(
            self.frame_entrada,
            text="Añadir tarea",
            width=12,
            command=self.agregar_tarea
        )
        self.btn_agregar.grid(row=0, column=1, padx=5)

        # -----------------------------
        # LISTBOX PARA MOSTRAR TAREAS
        # -----------------------------
        self.listbox_tareas = tk.Listbox(
            root,
            width=55,
            height=15,
            font=("Arial", 12),
            selectbackground="#a6d4fa",
            activestyle="none"
        )
        self.listbox_tareas.pack(pady=10)

        # -----------------------------
        # FRAME DE BOTONES
        # -----------------------------
        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(pady=10)

        self.btn_completar = tk.Button(
            self.frame_botones,
            text="Marcar completada",
            width=18,
            command=self.marcar_completada
        )
        self.btn_completar.grid(row=0, column=0, padx=5)

        self.btn_eliminar = tk.Button(
            self.frame_botones,
            text="Eliminar tarea",
            width=15,
            command=self.eliminar_tarea
        )
        self.btn_eliminar.grid(row=0, column=1, padx=5)

        # -----------------------------
        # ETIQUETA DE ATAJOS
        # -----------------------------
        self.label_atajos = tk.Label(
            root,
            text="Atajos: Enter = Añadir | C = Completar | Delete/D = Eliminar | Esc = Salir",
            font=("Arial", 10),
            fg="gray"
        )
        self.label_atajos.pack(pady=10)

        # -----------------------------
        # VINCULACIÓN DE EVENTOS
        # -----------------------------
        self.entry_tarea.bind("<Return>", self.agregar_tarea_evento)
        self.root.bind("<c>", self.marcar_completada_evento)
        self.root.bind("<C>", self.marcar_completada_evento)
        self.root.bind("<Delete>", self.eliminar_tarea_evento)
        self.root.bind("<d>", self.eliminar_tarea_evento)
        self.root.bind("<D>", self.eliminar_tarea_evento)
        self.root.bind("<Escape>", self.cerrar_aplicacion)

    def agregar_tarea(self):
        tarea = self.entry_tarea.get().strip()

        if tarea == "":
            messagebox.showwarning("Advertencia", "Por favor, escriba una tarea.")
            return

        self.tareas.append({"texto": tarea, "completada": False})
        self.actualizar_lista()
        self.entry_tarea.delete(0, tk.END)
        self.entry_tarea.focus()

    def agregar_tarea_evento(self, event):
        self.agregar_tarea()

    def marcar_completada(self):
        seleccion = self.listbox_tareas.curselection()

        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para marcarla.")
            return

        indice = seleccion[0]
        self.tareas[indice]["completada"] = True
        self.actualizar_lista()

    def marcar_completada_evento(self, event):
        self.marcar_completada()

    def eliminar_tarea(self):
        seleccion = self.listbox_tareas.curselection()

        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminarla.")
            return

        indice = seleccion[0]
        del self.tareas[indice]
        self.actualizar_lista()

    def eliminar_tarea_evento(self, event):
        self.eliminar_tarea()

    def cerrar_aplicacion(self, event=None):
        self.root.destroy()

    def actualizar_lista(self):
        self.listbox_tareas.delete(0, tk.END)

        for i, tarea in enumerate(self.tareas):
            if tarea["completada"]:
                texto_mostrar = f"✔ {tarea['texto']}  [COMPLETADA]"
                self.listbox_tareas.insert(tk.END, texto_mostrar)
                self.listbox_tareas.itemconfig(i, fg="green")
            else:
                texto_mostrar = f"• {tarea['texto']}  [PENDIENTE]"
                self.listbox_tareas.insert(tk.END, texto_mostrar)
                self.listbox_tareas.itemconfig(i, fg="black")


if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionTareas(root)
    root.mainloop()