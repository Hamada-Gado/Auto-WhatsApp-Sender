import tkinter as tk
from tkinter import messagebox
from threading import Thread

import gui
from exceptions import MyException

from .names import Names


class Main_Menu(tk.Frame):
    
    def __init__(self, *args, **kwargs):
        # from gui import Gui
        
        super().__init__(*args, **kwargs)
        
        self.master: gui.Gui
        self.title_font: tuple[str, int, str] = ("Arial", 26, "bold")
        self.font: tuple[str, int] = ("Arial", 18)
        
        self.title: tk.Label = tk.Label(self, text= self.master.title(), font= self.title_font)
        self.title.pack(side= tk.TOP, fill= tk.X)
        
        self.create_buttons()

    def create_buttons(self):
        self.buttons: tk.Frame = tk.Frame(self, bg= self["background"])
        tk.Button(self.buttons, text= "Run", font= self.font, command= self.auto_sender_run)
        tk.Button(self.buttons, text= Names.Settings.value, font= self.font, command= lambda : self.master.change_frame(Names.Settings))
        tk.Button(self.buttons, text= Names.Help.value, font= self.font, command= lambda : self.master.change_frame(Names.Help))
        
        for child in self.buttons.winfo_children():
            child.grid_configure(pady= 5)
        
        self.buttons.pack(anchor= tk.CENTER, expand= True)

    def auto_sender_run(self):
        def run():
            from pyautogui import FailSafeException
            try:
                self.master.auto_sender.run()
            except MyException as e:
                messagebox.showerror(title= self.master.title(), message= str(e)) 
            except FailSafeException:
                messagebox.showwarning(title= self.master.title(), message= "FailSafe triggered")
            except FileNotFoundError: # os handles it
                pass
            
        Thread(target= run).start()