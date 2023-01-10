import tkinter as tk
from .names import Names
import gui

class Main_Menu(tk.Frame):
    
    def __init__(self, *args, **kwargs):
        # from gui import Gui
        
        super().__init__(*args, **kwargs)
        
        self.master: gui.Gui
        self.title_font: tuple[str, int, str] = ("Arial", 24, "bold")
        self.font: tuple[str, int] = ("Arial", 18)
        
        self.title: tk.Label = tk.Label(self, text= "WhatsApp Auto Sender", font= self.title_font)
        self.title.pack(side= tk.TOP, fill= tk.X)
        
        self.set_buttons()

    def set_buttons(self):
        self.buttons: tk.Frame = tk.Frame(self, bg= self["background"])
        tk.Button(self.buttons, text= "Run", font= self.font, command= self.master.auto_sender.run)
        tk.Button(self.buttons, text= Names.Settings.value, font= self.font, command= lambda : self.master.change_frame(Names.Settings))
        tk.Button(self.buttons, text= Names.Help.value, font= self.font)
        
        for child in self.buttons.winfo_children():
            child.grid_configure(pady= 0.5)
        
        self.buttons.pack(anchor= tk.CENTER, expand= True)

    def change_to_settings(self):
        self.master.change_frame(Names.Settings)