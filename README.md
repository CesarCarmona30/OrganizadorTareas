# Organizador de Tareas

Una aplicación simple e interactiva para organizar tareas, construida con Python y Tkinter. Esta aplicación permite gestionar tareas añadiendo, editando y eliminandolas (CRUD sencillo). Las tareas se almacenan en un archivo JSON para garantizar persistencia.

## Funcionalidades

- Añadir tareas con título, categoría, notas y fecha límite.
- Editar o eliminar tareas existentes.
- Filtrar tareas por categoría.
- Almacenamiento persistente de tareas usando un archivo JSON.

## Requisitos previos

Asegúrate de tener lo siguiente instalado en tu sistema:

- **Python 3.10 o superior**
- **Tkinter** (incluido con Python)

## Instalación y Ejecución

1. Clona el repositorio en tu máquina local:

   ```bash
   git clone https://github.com/CesarCarmona30/OrganizadorTareas.git
   ```

2. Navega hasta el directorio

   ```
   cd OrganizadorTareas
   ```

3. (Opcional) Verifica que las dependencias estén instaladas (no se necesitan paquetes externos).

4. Navega hasta el directorio del proyecto

   ```bash
   cd Project
   ```

5. Ejecuta la aplicación:

   ```bash
   python app.py
   ```

## Estructura del proyecto

```bash
  OrganizadorTareas/
  ├── app.py                # Punto de entrada de la aplicación
  ├── db/                   # Dir: Almacenamiento persistente
  │   └── data.json         # Archivo JSON para almacenar tareas
  ├── model/                # Dir: Funcionalidad principal para los datos
  │   └── data_helper.py    # Validación de fechas, guardado y carga
  ├── view/                 # Dir: Componentes de la interfaz de usuario
  │   ├── styles.py         # Colores y fuentes
  │   ├── ui_controller.py  # Configuración de diseño, widgets y respuesta
  └── README.md             # Documentación del proyecto
```

## Uso

- Añadir una Tarea:
  Completa los campos de título, categoría, notas y fecha en el formulario, luego haz clic en "Add Task".

- Editar una Tarea:
  Selecciona una tarea de la lista y haz clic en "Edit" para actualizar sus detalles.

- Eliminar una Tarea:
  Selecciona una tarea de la lista y haz clic en "Delete" para eliminarla.

## Resolución de Problemas

Si la aplicación no se inicia:

- Asegúrate de tener instalado Python 3.10 o superior.
- Verifica que tienes instalado el módulo tkinter ejecutando:

  ```bash
  python -m tkinter
  ```

- Si el archivo JSON (data.json) está ausente o corrupto, elimínalo y reinicia la aplicación.
