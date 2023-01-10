import tkinter as tk
from .names import Names

class Main_Menu(tk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.font: tuple[str, int] = ("Arial", 18)
        self.set_buttons()

    def set_buttons(self):
        self.buttons: dict[Names | str, tk.Button] = dict()
        self.buttons["Auto Sender"] = tk.Button(self, text= "Run", font= self.font, bg= "blue", command= self.run_auto_sender)
        self.buttons[Names.Settings] = tk.Button(self, text= Names.Settings.value, font= self.font)
        
        for button in self.buttons.values():
            button.pack()
         
    def run_auto_sender(self):
        self.master.auto_sender.run() # type: ignore