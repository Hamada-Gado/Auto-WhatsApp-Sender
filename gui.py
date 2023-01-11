import tkinter as tk

import frames
from auto_sender import Auto_Sender
from data import Data   

class Gui(tk.Tk):
    WIDTH: int = 1000
    HEIGHT: int = 420
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        
        # Data and Automation class
        self.data: Data = Data()
        self.auto_sender: Auto_Sender = Auto_Sender(self.data)
        
        # creating base window
        self.geometry(f"{Gui.WIDTH}x{Gui.HEIGHT}")
        
        # creating frames
        self.current_frame: tk.Frame
        self.create_frames()
        
    def create_frames(self):
        self.frames: dict[frames.Names, tk.Frame] = dict()
        self.current_frame = self.frames[frames.Names.Main_Menu] = frames.Main_Menu(self, width= Gui.WIDTH, height= Gui.HEIGHT)
        self.frames[frames.Names.Settings] = frames.Settings(self)
        self.frames[frames.Names.Help] = frames.Help(self)
        
        self.current_frame.pack(expand= True, fill= tk.BOTH)

    def change_frame(self, frame_name: frames.Names):
        self.current_frame.pack_forget()
        self.current_frame = self.frames[frame_name]
        self.current_frame.pack(expand= True, fill= tk.BOTH)
    
    def run(self):
        self.mainloop()