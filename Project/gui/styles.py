from enum import Enum

# Estilos visuales para la interfaz
class Colors(Enum):
    BACKGROUND = "#24272b"
    TEXT = "#FFFFFF"
    BUTTON = "#61AFEF"
    BUTTON_HOVER = "#56B4E9"
    ALERT = "#d62839"
    LIST_BACKGROUND = "#4a525a"

class Fonts(Enum):
    TITLE = ("Bahnschrift", 20, "bold")
    TEXT = ("Trebuchet MS", 12)
    BUTTON = ("Bahnschrift", 12, "bold")

class Categories(Enum):
    ALL = ""
    SCHOOL = "Escuela"
    PERSONAL = "Personal"
    WORK = "Trabajo"