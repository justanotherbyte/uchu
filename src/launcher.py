import tkinter as tk
from typing import Tuple

import eel

from src.backend import init


# application setup related operations
init._application_initialize()


# launch related operations
allowed_extensions = [
    ".html",
    ".css",
    ".js",
    ".png",
    ".jpeg",
    ".jpg",
    ".webp"
]

def screen_size() -> Tuple[int, int]:
    tk_temp = tk.Tk("TEMPORARY")
    width = tk_temp.winfo_screenwidth()
    height = tk_temp.winfo_screenheight()
    del tk_temp
    return (width, height)


eel.init("./static", allowed_extensions=allowed_extensions)
eel.start("html/index.html", size=screen_size(), cmdline_args=['--start-fullscreen'])