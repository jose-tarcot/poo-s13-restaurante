# restaurante_app — Semana 13

**Estudiante:** José Alberto Tarco Tipán  
**Materia:** Programación Orientada a Objetos  
**Institución:** Universidad Estatal Amazónica  
**Entrega:** Semana 13 — Conceptos fundamentales de interfaces gráficas de usuario

---

## 1. Descripción general

Esta entrega inicia la transición de `restaurante_app` desde la consola hacia una **interfaz gráfica construida con Tkinter**, siguiendo la estructura base simplificada del proyecto docente *Biblioteca App*. Por ahora el sistema trabaja únicamente con **productos del menú** (con su tiempo de preparación) y **clientes por mesa**, que sirven además para simular el acceso al sistema. Las demás operaciones desarrolladas en semanas anteriores se recuperarán progresivamente.

---

## 2. Evolución del programa

```
ANTES
Mesero -> CLI -> Servicios -> Modelos -> JSON

AHORA
Mesero -> GUI -> Eventos -> Servicios -> Modelos -> JSON
```

La interfaz gráfica no reemplaza la arquitectura anterior: solo se encarga de la presentación y de los eventos. La lógica y el acceso a los datos siguen viviendo en los servicios.

---

## 3. Estructura del proyecto

```
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
└── main.py
```

---

## 4. Responsabilidad de cada capa

| Capa | Responsabilidad |
|---|---|
| `modelos/` | `Producto` (con tiempo de preparación) y `Usuario` (con mesa asignada), ambos con validaciones mediante `property`. |
| `servicios/archivo_servicio.py` | Lee y escribe los archivos JSON de `datos/`. |
| `servicios/restaurante_servicio.py` | Convierte los datos JSON en objetos, valida el acceso y expone las consultas que necesita la interfaz. |
| `ui/` | `LoginView` y `MainView`, construidas con Tkinter; solicitan la informacion a `RestauranteServicio`. |
| `main.py` | Crea la unica ventana principal y controla el cambio entre vistas. |

---

## 5. Flujo mínimo esperado

```
Inicio de la aplicacion
        ↓
main.py prepara Tkinter y los servicios
        ↓
LoginView (usuario y clave del cliente)
        ↓
RestauranteServicio valida el acceso
        ↓
MainView
        ↓
Menu | Clientes | Pedidos (pendiente) | Facturacion (pendiente)
        ↓
Cerrar sesion
        ↓
LoginView
```

---

## 6. Componentes Tkinter utilizados

`Tk`, `Frame`, `Label`, `Entry`, `ttk.Button`, `ttk.Style` y `messagebox` para las funcionalidades aun no implementadas graficamente (Pedidos, Facturacion).

---

## 7. Credenciales de acceso (demostración)

| Usuario | Contraseña |
|---|---|
| `jtarco` | `grill2026` |
| `admin` | `admin456` |

La contraseña debe incluir al menos un número, según la validación del modelo `Usuario`.

---

## 8. Ejecución

```bash
cd restaurante_app
python main.py
```

Requiere **Python 3.10 o superior** y Tkinter disponible en la instalación.

---

## 9. Pruebas realizadas

1. Se ejecuta `main.py` y la aplicación inicia sin errores.
2. La primera pantalla mostrada es `LoginView`.
3. Los campos de usuario y contraseña reciben texto correctamente.
4. Campos vacíos o credenciales incorrectas muestran un mensaje visual de error.
5. Con credenciales válidas se abre `MainView` dentro de la misma ventana.
6. La opción **Productos** muestra el menú cargado desde `productos.json`, incluyendo el tiempo de preparación.
7. La opción **Usuarios** muestra los clientes cargados desde `usuarios.json`, incluyendo su mesa asignada.
8. Las vistas obtienen la información desde `RestauranteServicio`, sin leer los archivos JSON directamente.
9. **Cerrar sesión** regresa a `LoginView` sin crear una ventana adicional.

---

## 10. Nota educativa sobre autenticación

El acceso de esta etapa es una simulación pedagógica. Las contraseñas se guardan en JSON en texto plano solo con fines didácticos; no representa una práctica segura para un sistema real.
