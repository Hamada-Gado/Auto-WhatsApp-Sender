import tkinter as tk

from data import Data


class Gui(tk.Tk):
    
    def __init__(self, main, data: Data, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.main = main
        self.data: Data = data