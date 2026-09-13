import tkinter as tk
from tkinter import messagebox, ttk


class MainView(tk.Frame):
    def __init__(self, master, restaurante_servicio, usuario_actual, al_cerrar_sesion):
        super().__init__(master, bg="#fffaf5")
        self.restaurante_servicio = restaurante_servicio
        self.usuario_actual = usuario_actual
        self.al_cerrar_sesion = al_cerrar_sesion
        self.contenido = None

        self.definir_estilos()
        self.construir_interfaz()

    def definir_estilos(self):
        # Colores y estilos reutilizables de la vista principal.
        self.color_fondo = "#fffaf5"
        self.color_encabezado = "#2b2320"
        self.color_texto = "#3d2f26"
        self.color_secundario = "#f0dcc4"
        self.color_resaltado = "#d97706"

        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure(
            "MenuApp.TButton",
            background=self.color_secundario,
            foreground=self.color_encabezado,
            font=("Arial", 10, "bold"),
            padding=(12, 8),
            borderwidth=0,
        )
        estilo.map("MenuApp.TButton", background=[("active", "#e6c69f")])
        estilo.configure(
            "CerrarSesion.TButton",
            background="#7a2e2e",
            foreground="#ffffff",
            font=("Arial", 10, "bold"),
            padding=(12, 8),
            borderwidth=0,
        )
        estilo.map("CerrarSesion.TButton", background=[("active", "#5f2323")])

    def construir_interfaz(self):
        # Construye la pantalla principal del sistema de mesas.
        encabezado = tk.Frame(self, bg=self.color_encabezado, padx=28, pady=18)
        encabezado.pack(fill="x")

        tk.Label(
            encabezado,
            text="PARRILLA DEL VALLE",
            bg=self.color_encabezado,
            fg="#ffffff",
            font=("Arial", 19, "bold"),
        ).pack(anchor="w")

        tk.Label(
            encabezado,
            text=f"Bienvenido, {self.usuario_actual.nombre} (Mesa: {self.usuario_actual.mesa})",
            bg=self.color_encabezado,
            fg="#f0dcc4",
            font=("Arial", 11),
        ).pack(anchor="w", pady=(6, 0))

        barra = tk.Frame(self, bg=self.color_secundario, padx=18, pady=10)
        barra.pack(fill="x")

        self.crear_boton_menu(barra, "Productos", self.mostrar_productos)
        self.crear_boton_menu(barra, "Usuarios", self.mostrar_usuarios)
        self.crear_boton_menu(barra, "Pedidos", self.mostrar_funcionalidad_pendiente)
        self.crear_boton_menu(barra, "Facturacion", self.mostrar_funcionalidad_pendiente)

        ttk.Button(
            barra,
            text="Cerrar sesion",
            command=self.cerrar_sesion,
            style="CerrarSesion.TButton",
        ).pack(side="right")

        self.contenido = tk.Frame(self, bg=self.color_fondo, padx=28, pady=24)
        self.contenido.pack(fill="both", expand=True)

        self.mostrar_inicio()
        self.crear_barra_estado()

    def crear_boton_menu(self, contenedor, texto, comando):
        # Agrega una opcion visual en la barra superior.
        ttk.Button(
            contenedor,
            text=texto,
            command=comando,
            style="MenuApp.TButton",
        ).pack(side="left", padx=(0, 8))

    def limpiar_contenido(self):
        # Limpia el area central antes de mostrar una nueva seccion.
        assert self.contenido is not None

        for widget in self.contenido.winfo_children():
            widget.destroy()

    def mostrar_inicio(self):
        # Estado inicial de la interfaz principal.
        self.limpiar_contenido()

        assert self.contenido is not None

        tk.Label(
            self.contenido,
            text="Panel de mesero",
            bg=self.color_fondo,
            fg=self.color_encabezado,
            font=("Arial", 18, "bold"),
        ).pack(anchor="w", pady=(0, 8))

        tk.Label(
            self.contenido,
            text="Seleccione una opcion superior para ver la informacion cargada.",
            bg=self.color_fondo,
            fg=self.color_texto,
            font=("Arial", 12),
        ).pack(anchor="w")

    def mostrar_productos(self):
        # Pide el menu al servicio y lo despliega en pantalla.
        self.limpiar_contenido()

        assert self.contenido is not None

        self.crear_titulo_seccion("Menu disponible")

        for producto in self.restaurante_servicio.listar_productos():
            texto = (
                f"{producto.codigo} - {producto.nombre} | {producto.categoria} | "
                f"${producto.precio:.2f} | {producto.resumen_tiempo()} | Stock: {producto.stock}"
            )
            self.crear_fila_informacion(texto)

    def mostrar_usuarios(self):
        # Pide los clientes registrados al servicio y los despliega en pantalla.
        self.limpiar_contenido()

        assert self.contenido is not None

        self.crear_titulo_seccion("Clientes registrados")

        for usuario in self.restaurante_servicio.listar_usuarios():
            texto = f"{usuario.identificacion} - {usuario.nombre} | Mesa: {usuario.mesa}"
            self.crear_fila_informacion(texto)

    def crear_titulo_seccion(self, texto):
        # Presenta el titulo de la seccion seleccionada.
        assert self.contenido is not None

        tk.Label(
            self.contenido,
            text=texto,
            bg=self.color_fondo,
            fg=self.color_encabezado,
            font=("Arial", 17, "bold"),
        ).pack(anchor="w", pady=(0, 14))

    def crear_fila_informacion(self, texto):
        # Fila simple sin tablas avanzadas.
        assert self.contenido is not None

        fila = tk.Frame(self.contenido, bg="#ffffff", padx=14, pady=10)
        fila.pack(fill="x", pady=(0, 8))

        tk.Label(
            fila,
            text=texto,
            bg="#ffffff",
            fg=self.color_texto,
            font=("Arial", 11),
        ).pack(anchor="w")

    def crear_barra_estado(self):
        # Barra inferior con el estado general del sistema.
        barra_estado = tk.Frame(self, bg=self.color_secundario, padx=18, pady=8)
        barra_estado.pack(fill="x", side="bottom")

        tk.Label(
            barra_estado,
            text=(
                f"Productos: {self.restaurante_servicio.cantidad_productos()} | "
                f"Clientes: {self.restaurante_servicio.cantidad_usuarios()} | "
                "Informacion cargada desde archivos JSON"
            ),
            bg=self.color_secundario,
            fg=self.color_texto,
            font=("Arial", 10),
        ).pack(side="left")

    def mostrar_funcionalidad_pendiente(self):
        messagebox.showinfo(
            "Proximamente",
            "Esta funcionalidad se incorporara en una proxima entrega.",
        )

    def cerrar_sesion(self):
        # Regresa al login dentro de la misma ventana.
        self.al_cerrar_sesion()
