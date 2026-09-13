from modelos.producto import Producto
from modelos.usuario import Usuario


class RestauranteServicio:
    def __init__(self, archivo_servicio) -> None:
        self.archivo_servicio = archivo_servicio
        self.usuarios: list[Usuario] = []
        self.productos: list[Producto] = []
        self.cargar_datos()

    def cargar_datos(self) -> None:
        # Convierte los registros de usuarios.json y productos.json en objetos del dominio.
        usuarios_json = self.archivo_servicio.leer_json("usuarios.json")
        productos_json = self.archivo_servicio.leer_json("productos.json")

        self.usuarios = []
        for datos in usuarios_json:
            try:
                usuario = Usuario(
                    datos.get("identificacion", ""),
                    datos.get("nombre", ""),
                    datos.get("mesa", ""),
                    datos.get("usuario", ""),
                    datos.get("contrasena", ""),
                )
                self.usuarios.append(usuario)
            except ValueError as error:
                print(f"Cliente con datos invalidos, se omite: {error}")

        self.productos = []
        for datos in productos_json:
            try:
                producto = Producto(
                    datos.get("codigo", ""),
                    datos.get("nombre", ""),
                    datos.get("precio", 0),
                    datos.get("categoria", ""),
                    datos.get("tiempo_preparacion", 10),
                    datos.get("stock", 0),
                )
                self.productos.append(producto)
            except ValueError as error:
                print(f"Producto con datos invalidos, se omite: {error}")

    def validar_acceso(self, usuario: str, contrasena: str) -> Usuario | None:
        # Recorre los clientes cargados y delega la comparacion de credenciales.
        for usuario_registrado in self.usuarios:
            if usuario_registrado.validar_credenciales(usuario, contrasena):
                return usuario_registrado
        return None

    def listar_usuarios(self) -> list[Usuario]:
        return self.usuarios.copy()

    def listar_productos(self) -> list[Producto]:
        return self.productos.copy()

    def cantidad_usuarios(self) -> int:
        return len(self.usuarios)

    def cantidad_productos(self) -> int:
        return len(self.productos)

    def consultar_cantidad_producto(self, codigo: str) -> int | None:
        # Permite consultar el stock disponible de un plato especifico.
        codigo_normalizado = codigo.strip().upper()
        for producto in self.productos:
            if producto.codigo == codigo_normalizado:
                return producto.stock
        return None
