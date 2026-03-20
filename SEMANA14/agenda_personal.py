import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class AgendaPersonalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("1000x620")
        self.root.resizable(False, False)
        self.root.configure(bg="#EEF3F8")

        self.contador_eventos = 1

        self.configurar_estilos()
        self.crear_interfaz()

    def configurar_estilos(self):
        """Configura los estilos visuales de los widgets ttk."""
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Estilo del Treeview
        self.style.configure(
            "Treeview",
            background="#FFFFFF",
            foreground="#1F2937",
            rowheight=30,
            fieldbackground="#FFFFFF",
            font=("Segoe UI", 10)
        )

        self.style.configure(
            "Treeview.Heading",
            background="#2A6F97",
            foreground="white",
            font=("Segoe UI", 10, "bold"),
            relief="flat"
        )

        self.style.map(
            "Treeview",
            background=[("selected", "#BDE0FE")],
            foreground=[("selected", "#000000")]
        )

        self.style.configure(
            "Vertical.TScrollbar",
            gripcount=0,
            background="#A8DADC",
            darkcolor="#A8DADC",
            lightcolor="#A8DADC",
            troughcolor="#F1F5F9",
            bordercolor="#F1F5F9",
            arrowcolor="#1D3557"
        )

    def crear_interfaz(self):
        """Construye la interfaz gráfica principal."""
        # =========================
        # ENCABEZADO
        # =========================
        header = tk.Frame(self.root, bg="#1D3557", height=100)
        header.pack(fill="x")

        titulo = tk.Label(
            header,
            text="Agenda Personal",
            font=("Segoe UI", 24, "bold"),
            bg="#1D3557",
            fg="white"
        )
        titulo.place(relx=0.5, rely=0.35, anchor="center")

        subtitulo = tk.Label(
            header,
            text="Organiza tus eventos y tareas de forma práctica, clara y elegante",
            font=("Segoe UI", 11),
            bg="#1D3557",
            fg="#D6E6F2"
        )
        subtitulo.place(relx=0.5, rely=0.70, anchor="center")

        # =========================
        # CONTENEDOR PRINCIPAL
        # =========================
        contenedor = tk.Frame(self.root, bg="#EEF3F8")
        contenedor.pack(fill="both", expand=True, padx=20, pady=20)

        # =========================
        # PANEL IZQUIERDO
        # =========================
        panel_izquierdo = tk.Frame(
            contenedor,
            bg="white",
            bd=0,
            relief="flat",
            highlightbackground="#D9E2EC",
            highlightthickness=1
        )
        panel_izquierdo.pack(side="left", fill="y", padx=(0, 18))

        titulo_form = tk.Label(
            panel_izquierdo,
            text="Nuevo evento o tarea",
            font=("Segoe UI", 16, "bold"),
            bg="white",
            fg="#1D3557"
        )
        titulo_form.pack(pady=(20, 18), padx=20)

        # Frame interno del formulario
        form = tk.Frame(panel_izquierdo, bg="white")
        form.pack(padx=22, pady=5)

        # Fecha
        tk.Label(
            form,
            text="Fecha:",
            font=("Segoe UI", 11, "bold"),
            bg="white",
            fg="#334E68"
        ).pack(anchor="w", pady=(0, 6))

        self.date_entry = DateEntry(
            form,
            width=24,
            background="#2A6F97",
            foreground="white",
            borderwidth=2,
            date_pattern="dd/mm/yyyy",
            font=("Segoe UI", 10)
        )
        self.date_entry.pack(pady=(0, 16), ipady=3)

        # Hora
        tk.Label(
            form,
            text="Hora (HH:MM):",
            font=("Segoe UI", 11, "bold"),
            bg="white",
            fg="#334E68"
        ).pack(anchor="w", pady=(0, 6))

        self.entry_hora = tk.Entry(
            form,
            font=("Segoe UI", 11),
            width=28,
            bd=1,
            relief="solid",
            highlightthickness=1,
            highlightbackground="#BCCCDC"
        )
        self.entry_hora.pack(pady=(0, 16), ipady=6)

        # Descripción
        tk.Label(
            form,
            text="Descripción:",
            font=("Segoe UI", 11, "bold"),
            bg="white",
            fg="#334E68"
        ).pack(anchor="w", pady=(0, 6))

        self.entry_descripcion = tk.Entry(
            form,
            font=("Segoe UI", 11),
            width=28,
            bd=1,
            relief="solid",
            highlightthickness=1,
            highlightbackground="#BCCCDC"
        )
        self.entry_descripcion.pack(pady=(0, 22), ipady=6)

        # Botones
        frame_botones = tk.Frame(panel_izquierdo, bg="white")
        frame_botones.pack(pady=(5, 20))

        btn_agregar = tk.Button(
            frame_botones,
            text="Agregar Evento",
            font=("Segoe UI", 10, "bold"),
            bg="#2A9D8F",
            fg="white",
            activebackground="#21867A",
            activeforeground="white",
            width=24,
            height=2,
            relief="flat",
            cursor="hand2",
            command=self.agregar_evento
        )
        btn_agregar.pack(pady=8)

        btn_eliminar = tk.Button(
            frame_botones,
            text="Eliminar Seleccionado",
            font=("Segoe UI", 10, "bold"),
            bg="#E76F51",
            fg="white",
            activebackground="#D8573C",
            activeforeground="white",
            width=24,
            height=2,
            relief="flat",
            cursor="hand2",
            command=self.eliminar_evento
        )
        btn_eliminar.pack(pady=8)

        btn_salir = tk.Button(
            frame_botones,
            text="Salir",
            font=("Segoe UI", 10, "bold"),
            bg="#6C757D",
            fg="white",
            activebackground="#5A6268",
            activeforeground="white",
            width=24,
            height=2,
            relief="flat",
            cursor="hand2",
            command=self.root.quit
        )
        btn_salir.pack(pady=8)

        # =========================
        # PANEL DERECHO
        # =========================
        panel_derecho = tk.Frame(
            contenedor,
            bg="white",
            bd=0,
            relief="flat",
            highlightbackground="#D9E2EC",
            highlightthickness=1
        )
        panel_derecho.pack(side="right", fill="both", expand=True)

        titulo_tabla = tk.Label(
            panel_derecho,
            text="Eventos programados",
            font=("Segoe UI", 16, "bold"),
            bg="white",
            fg="#1D3557"
        )
        titulo_tabla.pack(pady=(20, 15))

        descripcion_tabla = tk.Label(
            panel_derecho,
            text="Aquí se muestran los eventos registrados en la agenda.",
            font=("Segoe UI", 10),
            bg="white",
            fg="#577590"
        )
        descripcion_tabla.pack(pady=(0, 15))

        tabla_frame = tk.Frame(panel_derecho, bg="white")
        tabla_frame.pack(fill="both", expand=True, padx=18, pady=(0, 18))

        self.tree = ttk.Treeview(
            tabla_frame,
            columns=("ID", "Fecha", "Hora", "Descripción"),
            show="headings",
            height=16
        )

        self.tree.heading("ID", text="ID")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")

        self.tree.column("ID", width=60, anchor="center")
        self.tree.column("Fecha", width=130, anchor="center")
        self.tree.column("Hora", width=110, anchor="center")
        self.tree.column("Descripción", width=420, anchor="w")

        scrollbar = ttk.Scrollbar(tabla_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Eventos de ejemplo
        self.insertar_evento_inicial("15/03/2026", "08:00", "Clase de Programación Orientada a Objetos")
        self.insertar_evento_inicial("16/03/2026", "14:30", "Reunión de proyecto final")
        self.insertar_evento_inicial("17/03/2026", "19:00", "Estudiar Tkinter y TreeView")

    def insertar_evento_inicial(self, fecha, hora, descripcion):
        """Inserta eventos de ejemplo al iniciar la aplicación."""
        self.tree.insert("", "end", values=(self.contador_eventos, fecha, hora, descripcion))
        self.contador_eventos += 1

    def validar_hora(self, hora):
        """Valida que la hora tenga formato HH:MM y esté en rango válido."""
        try:
            partes = hora.split(":")
            if len(partes) != 2:
                return False

            hh = int(partes[0])
            mm = int(partes[1])

            return 0 <= hh <= 23 and 0 <= mm <= 59
        except ValueError:
            return False

    def agregar_evento(self):
        """Agrega un nuevo evento al TreeView tras validar los datos."""
        fecha = self.date_entry.get()
        hora = self.entry_hora.get().strip()
        descripcion = self.entry_descripcion.get().strip()

        if not hora or not descripcion:
            messagebox.showwarning(
                "Campos incompletos",
                "Debe ingresar la hora y la descripción del evento."
            )
            return

        if not self.validar_hora(hora):
            messagebox.showerror(
                "Hora inválida",
                "La hora debe estar en formato HH:MM.\nEjemplo: 09:30"
            )
            return

        self.tree.insert("", "end", values=(self.contador_eventos, fecha, hora, descripcion))
        self.contador_eventos += 1

        messagebox.showinfo("Éxito", "El evento fue agregado correctamente.")

        self.entry_hora.delete(0, tk.END)
        self.entry_descripcion.delete(0, tk.END)
        self.entry_hora.focus()

    def eliminar_evento(self):
        """Elimina el evento seleccionado con confirmación previa."""
        seleccionado = self.tree.selection()

        if not seleccionado:
            messagebox.showwarning(
                "Sin selección",
                "Seleccione un evento de la tabla para eliminar."
            )
            return

        confirmar = messagebox.askyesno(
            "Confirmar eliminación",
            "¿Está seguro de que desea eliminar el evento seleccionado?"
        )

        if confirmar:
            self.tree.delete(seleccionado)
            messagebox.showinfo("Eliminado", "El evento fue eliminado correctamente.")


if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaPersonalApp(root)
    root.mainloop()