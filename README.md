# Organizador de Tareas

Una aplicación simple e interactiva para organizar tareas, construida con Python y Tkinter. Esta aplicación te permite gestionar tus tareas añadiendo, editando, eliminando y filtrándolas. Las tareas se almacenan en un archivo JSON para garantizar persistencia.

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
   cd OrganizadorTareas
   ```

2. (Opcional) Verifica que las dependencias estén instaladas (no se necesitan paquetes externos).

3. Navega hasta el directorio del proyecto

   ```bash
   cd Project
   ```

4. Ejecuta la aplicación:

   ```bash
   python app.py
   ```

## Estructura del proyecto

```bash
  OrganizadorTareas/
  ├── main.py              # Punto de entrada de la aplicación
  ├── gui/                 # Componentes de la interfaz de usuario
  │   ├── styles.py        # Colores, fuentes y estilos
  │   ├── ui.py            # Configuración de diseño y widgets
  ├── core/                # Funcionalidad principal y lógica
  │   └── tasks.py         # Validación de tareas, guardado y carga
  ├── data/                # Almacenamiento persistente
  │   └── tasks.json       # Archivo JSON para almacenar tareas
  └── README.md            # Documentación del proyecto
```

## Uso

- Añadir una Tarea:
  Completa los campos de título, categoría, notas y fecha en el formulario, luego haz clic en "Add Task".

- Editar una Tarea:
  Selecciona una tarea de la lista y haz clic en "Edit" para actualizar sus detalles.

- Eliminar una Tarea:
  Selecciona una tarea de la lista y haz clic en "Delete" para eliminarla.

- Filtrar Tareas:
  Usa el menú desplegable de categorías para filtrar las tareas.

## Resolución de Problemas

Si la aplicación no se inicia:

- Asegúrate de tener instalado Python 3.10 o superior.
- Verifica que tienes instalado el módulo tkinter ejecutando:

  ```bash
  python -m tkinter
  ```

- Si el archivo JSON (tasks.json) está ausente o corrupto, elimínalo y reinicia la aplicación.
