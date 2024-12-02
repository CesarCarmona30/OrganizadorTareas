from enum import Enum

# Estilos visuales para la interfaz
class Colors(Enum):
    BACKGROUND = "#00843D"
    TEXT = "#000000"
    BUTTON = "#EEEF20"
    BUTTON_HOVER = "#000000"
    FILTER = "#98C379"
    ALERT = "#EEEF20"
    LIST_BACKGROUND = "#eff1ed"

class Fonts(Enum):
    TITLE = ("Arial", 20, "bold")
    TEXT = ("Arial", 12)
    BUTTON = ("Arial", 12, "bold")

class Categories(Enum):
    ALL = ""
    SCHOOL = "Escuela"
    PERSONAL = "Personal"
    WORK = "Trabajo"