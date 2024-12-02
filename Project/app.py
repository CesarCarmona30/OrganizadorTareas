import tkinter as tk
from core.tasks import load_tasks, save_tasks, validate_date
from gui.styles import Colors
from gui.ui import configure_styles, create_widgets, update_task, delete_task

def create_task(entries, treeview):
    """Crea y añade una nueva tarea a la lista."""
    title = entries["titulo"].get().strip()
    category = entries["categoria"].get().strip()
    notes = entries["notas"].get("1.0", tk.END).strip()
    date = entries["fecha"].get().strip()

    if not title or not category or not date:
        tk.messagebox.showwarning("Campos vacíos", "Título, categoría y fecha son obligatorios.")
        return

    if not validate_date(date):
        tk.messagebox.showwarning("Fecha inválida", "La fecha debe estar en el formato dd/mm.")
        return

    treeview.insert("", "end", values=(title, category, notes, date))
    for entry in entries.values():
        if isinstance(entry, tk.Text):
            entry.delete("1.0", tk.END)
        else:
            entry.delete(0, tk.END)
    save_tasks(treeview)

# Punto de entrada para el programa 
def main():
    root = tk.Tk()
    root.title("Organizador de tareas")
    root.geometry("1000x540")
    root.configure(bg=Colors.BACKGROUND.value)

    configure_styles()
    treeview = create_widgets(
        root,
        create_task,
        update_task,
        delete_task
    )

    load_tasks(treeview)

    root.mainloop()

if __name__ == "__main__":
    main()