"""
The MIT License (MIT)

Copyright (c) 2021-present justanotherbyte

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import tkinter as tk
from typing import Tuple

import eel


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
eel.start("html/index.html", size=screen_size())