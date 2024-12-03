import tkinter as tk
from core.tasks import read_tasks
from gui.styles import Colors
from gui.ui import configure_styles, create_widgets, update_task, delete_task, create_task

# Punto de entrada para el programa 
def main():
    root = tk.Tk()
    root.title("Organizador de tareas")
    root.geometry("1000x580")
    root.configure(bg=Colors.BACKGROUND.value)

    configure_styles()
    treeview = create_widgets(
        root,
        create_task,
        update_task,
        delete_task
    )

    read_tasks(treeview)

    root.mainloop()

if __name__ == "__main__":
    main()