import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.simpledialog import askstring
from gui.styles import Colors, Fonts, Categories
from core.tasks import save_tasks, validate_date

def create_task(entries, treeview):
    """Crea y añade una nueva tarea a la lista."""
    title = entries["titulo"].get().strip()
    category = entries["categoria"].get().strip()
    notes = entries["notas"].get("1.0", tk.END).strip()
    date = entries["fecha"].get().strip()

    if not title or not category or not date:
        messagebox.showwarning("Campos vacíos", "Título, categoría y fecha son obligatorios.")
        return

    if not validate_date(date):
        messagebox.showwarning("Fecha inválida", "La fecha debe estar en el formato dd/mm.")
        return

    treeview.insert("", "end", values=(title, category, notes, date))
    for entry in entries.values():
        if isinstance(entry, tk.Text):
            entry.delete("1.0", tk.END)
        else:
            entry.delete(0, tk.END)
    save_tasks(treeview)

def update_task(treeview):
    """Editar la tarea seleccionada."""
    try:
        selected_item = treeview.selection()[0]
        values = treeview.item(selected_item, "values")
        new_title = askstring("Editar título", "Nuevo título:", initialvalue=values[0])
        new_category = askstring("Editar categoría", "Nueva categoría:", initialvalue=values[1])
        new_notes = askstring("Editar notas", "Nuevas notas:", initialvalue=values[2])
        new_date = askstring("Editar fecha", "Nueva fecha:", initialvalue=values[3])
        new_date = new_date if validate_date(new_date) else values[3]

        if new_title and new_category and new_date:
            treeview.item(selected_item, values=(new_title, new_category, new_notes, new_date))
            save_tasks(treeview) 
    except IndexError:
        messagebox.showwarning("Sin selección", "Por favor, selecciona una tarea para editar.")
        
def delete_task(treeview):
    """Elimina la tarea seleccionada"""
    try:
        selected_item = treeview.selection()[0]
        confirm = messagebox.askyesno("Confirmación", "¿Está seguro de querer elimnar esta tarea?")
        if confirm:
            treeview.delete(selected_item)
            save_tasks(treeview)
    except IndexError:
        messagebox.showwarning("Sin selección", "Por favor, selecciona una tarea para eliminar.")


def configure_styles():
    """Configura los estilos visuales de la interfaz."""
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview",
                    background=Colors.LIST_BACKGROUND.value,
                    fieldbackground=Colors.LIST_BACKGROUND.value,
                    foreground=Colors.TEXT.value,
                    font=Fonts.TEXT.value)
    style.configure("Treeview.Heading",
                    font=Fonts.BUTTON.value)

def create_widgets(root, add_task, update_task, delete_task):
    """Crea e inicializa los elementos principales."""
    main_frame = tk.Frame(root, bg=Colors.BACKGROUND.value)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Lista de tareas
    task_frame = tk.Frame(main_frame, bg=Colors.BACKGROUND.value, height=100)
    task_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    title_list = tk.Label(task_frame, text="Lista de Tareas", font=Fonts.TITLE.value, bg=Colors.BACKGROUND.value, fg=Colors.TEXT.value)
    title_list.pack(anchor="w", pady=5)

    columns = ("Título", "Categoría", "Notas", "Fecha")
    treeview = ttk.Treeview(task_frame, columns=columns, show="headings", height=20)
    for col in columns:
        treeview.heading(col, text=col)
        treeview.column(col, width=100 if col == "Fecha" else 200)
    treeview.pack(fill=tk.BOTH, expand=True)

    # Botones para acciones
    action_buttons = tk.Frame(task_frame, bg=Colors.BACKGROUND.value)
    action_buttons.pack(pady=10)

    btn_edit = tk.Button(action_buttons, text="Editar", command=lambda: update_task(treeview), 
                         font=Fonts.BUTTON.value, bg=Colors.BUTTON.value)
    btn_edit.grid(row=0, column=0, padx=5)

    btn_delete = tk.Button(action_buttons, text="Eliminar", command=lambda: delete_task(treeview), 
                           font=Fonts.BUTTON.value, bg=Colors.ALERT.value)
    btn_delete.grid(row=0, column=1, padx=5)

    # Formulario para añadir tareas
    form_frame = tk.Frame(main_frame, bg=Colors.BACKGROUND.value)
    form_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=10, pady=10)

    title_form = tk.Label(form_frame, text="Agregar Tarea", font=Fonts.TITLE.value, bg=Colors.BACKGROUND.value, fg=Colors.TEXT.value)
    title_form.pack(anchor="w", pady=5)

    form_entries = {}
    for label_text, key in [("Título:", "titulo"), ("Categoría:", "categoria"), ("Notas:", "notas"), ("Fecha (dd/mm):", "fecha")]:
        label = tk.Label(form_frame, text=label_text, font=Fonts.TEXT.value, bg=Colors.BACKGROUND.value, fg=Colors.TEXT.value)
        label.pack(anchor="w", pady=2)
        if key == "notas":
            entry = tk.Text(form_frame, height=5, font=Fonts.TEXT.value)
        elif key == "categoria":
            entry = ttk.Combobox(form_frame, values=[c.value for c in Categories][1:], font=Fonts.TEXT.value)
        else:
            entry = tk.Entry(form_frame, font=Fonts.TEXT.value)
        entry.pack(fill=tk.X, pady=2)
        form_entries[key] = entry

    btn_add = tk.Button(form_frame, text="Agregar Tarea", command=lambda: add_task(form_entries, treeview), 
                        font=Fonts.BUTTON.value, bg=Colors.BUTTON.value)
    btn_add.pack(pady=5)

    treeview.bind("<Double-1>", lambda event: show_complete_notes(event, treeview, root))

    return treeview

def show_complete_notes(event, treeview, root):
    """Muestra el contenido completo de las notas."""
    selected_item = treeview.selection()
    if selected_item:
        values = treeview.item(selected_item[0], "values")
        notes = values[2] 
        if notes:
            notes_window = tk.Toplevel(root)
            notes_window.title("Notas completas")
            notes_window.geometry("400x300")
            notes_window.configure(bg=Colors.BACKGROUND.value)
            text = tk.Text(notes_window, font=Fonts.TEXT.value, wrap=tk.WORD, bg=Colors.BACKGROUND.value, fg=Colors.TEXT.value)
            text.insert("1.0", notes)
            text.config(state=tk.DISABLED)
            text.pack(fill=tk.BOTH, expand=True)
