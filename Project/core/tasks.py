import json
from datetime import datetime
from tkinter import messagebox

FILE_NAME = "./Project/data/tasks.json"

def validate_date(date):
    """Verifica que la fecha tenga el formato correcto (dd/mm)."""
    try:
        datetime.strptime(date, "%d/%m")
        return True
    except ValueError:
        return False

def load_tasks(treeview):
    """Carga las tareas desde el archivo JSON."""
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            tasks = json.load(file)
            for task in tasks:
                treeview.insert("", "end", 
                                values=(task["titulo"], 
                                        task["categoria"], 
                                        task["notas"], 
                                        task["fecha"]))
    except (FileNotFoundError, json.JSONDecodeError):
        pass

def save_tasks(treeview):
    """Guarda las tareas en el archivo JSON."""
    tasks = []
    for item_id in treeview.get_children():
        item = treeview.item(item_id)
        values = item["values"]
        if len(values) == 4:
            tasks.append({
                "titulo": values[0],
                "categoria": values[1],
                "notas": values[2],
                "fecha": values[3],
            })

    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(tasks, file, ensure_ascii=False, indent=4)
    except IOError as e:
        messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")
