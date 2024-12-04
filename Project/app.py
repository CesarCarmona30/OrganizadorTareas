import tkinter as tk
import view
from model.data_helper import read_data
from view.ui_controller import configure_styles, create_widgets, update_task, delete_task, create_task

# Punto de entrada para el programa 
def main():
    root = tk.Tk()
    root.title("Organizador de tareas")
    root.geometry("1000x580")
    root.configure(bg=view.styles.Colors.BACKGROUND.value)

    configure_styles()
    treeview = create_widgets(
        root,
        create_task,
        update_task,
        delete_task
    )

    read_data(treeview)

    root.mainloop()

if __name__ == "__main__":
    main()