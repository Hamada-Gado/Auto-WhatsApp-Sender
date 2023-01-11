from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

from PIL import Image

import gui

from .names import Names


class Settings(tk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.master: gui.Gui
        
        self.label_font: tuple[str, int, str] = ("Arial", 20, "bold")
        self.font: tuple[str, int] = ("Arial", 18)

        self.create_frames()
        
    def pack(self, *args, **kwargs):
        super().pack(*args, **kwargs)
        self.update_vars()
    
    def create_frames(self):
        self.create_top_frame()
        self.create_bot_frame()
        
    def create_bot_frame(self):
        self.bot_frame: tk.Frame = tk.Frame(self)
        
        tk.Button(self.bot_frame, text= "Save", font= self.font, command= self.save).grid(row= 0, column= 0)
        tk.Button(self.bot_frame, text= "Load Default", font= self.font, command= self.load_default).grid(row= 0, column= 1)
        tk.Button(self.bot_frame, text= "Back", font= self.font, command= lambda : self.master.change_frame(Names.Main_Menu)).grid(row= 0, column= 2)
         
        for child in self.bot_frame.winfo_children():
            child.grid_configure(padx= 10)
        
        self.bot_frame.pack(side= tk.BOTTOM, anchor= tk.CENTER)
        
    def load_default(self):
        self.master.data.load_default()
        self.update_vars()
    
    def update_vars(self):
        self.whatsApp_var.set(self.master.data.whatsApp_path.as_posix())
        
        self.options_list = self.master.data.names.copy()
        self.options_var.set('')
        self.option_menu['menu'].delete(0,'end')
        for name in self.master.data.names: 
            self.option_menu['menu'].add_command(label= name, command=tk._setit(self.options_var, name))
        
        if isinstance(self.master.data.message, str):
            self.message_var.set(self.master.data.message)
        else:
            self.message_var.set("")
            
        self.online_var.set(self.master.data.online)
        
        self.min_wait_time_var.set(self.master.data.min_wait_time)
        
        self.interval_var.set(self.master.data.interval)
        
    def save(self):
        try:
            self.master.data.min_wait_time = self.min_wait_time_var.get()
        except tk.TclError:
            messagebox.showerror(title= self.master.title(), message= "Min Wait Time expect a number")     
            return
        
        try:
            self.master.data.interval = self.interval_var.get()
        except tk.TclError:
            messagebox.showerror(title= self.master.title(), message= "Interval expect a number")     
            return
        
        self.master.data.whatsApp_path = Path(self.whatsApp_var.get())
        self.master.data.names = self.options_list.copy()
        if self.message_var.get() != "":
            self.master.data.message = self.message_var.get()
        self.master.data.online = self.online_var.get()
        
        self.master.data.save()
        
    def create_top_frame(self):
        self.top_frame: tk.Frame = tk.Frame(self)
        
        # whatsApp path
        tk.Label(self.top_frame, text= "WhatsApp Path", font= self.label_font).grid(row= 0, column= 0)
        self.whatsApp_var: tk.StringVar = tk.StringVar(None, self.master.data.whatsApp_path.as_posix())
        tk.Entry(self.top_frame, textvariable= self.whatsApp_var, font= self.font).grid(row= 0, column= 1)
        
        # names list
        tk.Label(self.top_frame, text= "Names", font= self.label_font).grid(row= 1, column= 0)
        
        self.names_left_frame: tk.Frame = tk.Frame(self.top_frame)
        self.name_var: tk.StringVar = tk.StringVar()
        tk.Entry(self.names_left_frame, textvariable= self.name_var, font= self.font).grid(row= 0, column= 0)
        self.names_left_frame.grid(row= 1, column= 1)        
        
        self.names_right_frame: tk.Frame = tk.Frame(self.top_frame)
        self.options_list: list[str] = self.master.data.names.copy()
        self.options_var: tk.StringVar = tk.StringVar()
        self.option_menu: tk.OptionMenu = tk.OptionMenu(self.names_right_frame, self.options_var, "", *self.options_list)
        self.option_menu.grid(row= 0, column= 0)
        tk.Button(self.names_right_frame, text= "Add", font= self.font, command= self.add_option).grid(row= 0, column= 1)
        tk.Button(self.names_right_frame, text= "Remove", font= self.font, command= self.remove_selected_option).grid(row= 0, column= 2)
        
        self.names_right_frame.grid(row= 1, column= 2)
        
        # message to send
        tk.Label(self.top_frame, text= "Message", font= self.label_font).grid(row= 2, column= 0)
        self.message_var: tk.StringVar = tk.StringVar(None, self.master.data.message if isinstance(self.master.data.message, str) else "")
        tk.Entry(self.top_frame, textvariable= self.message_var, font= self.font).grid(row= 2, column= 1)
        tk.Button(self.top_frame, text= "Set Image", font= self.font, command= self.set_image).grid(row= 2, column= 2)
        
        # online method or not
        tk.Label(self.top_frame, text= "Online", font= self.label_font).grid(row= 3, column= 0)
        self.online_var: tk.BooleanVar = tk.BooleanVar(None, self.master.data.online)
        tk.Radiobutton(self.top_frame, indicatoron= False, text= "True", font= self.font, variable= self.online_var, value= True).grid(row= 3, column= 1)
        tk.Radiobutton(self.top_frame, indicatoron= False, text= "False", font= self.font,  variable= self.online_var, value= False).grid(row= 3, column= 2)
        
        # min wait time
        tk.Label(self.top_frame, text= "Min Wait Time", font= self.label_font).grid(row= 4, column= 0)
        self.min_wait_time_var: tk.DoubleVar = tk.DoubleVar(None, self.master.data.min_wait_time)
        tk.Entry(self.top_frame, textvariable= self.min_wait_time_var, font= self.font).grid(row= 4, column= 1)
        
        # internal interval
        tk.Label(self.top_frame, text= "Interval", font= self.label_font).grid(row= 5, column= 0)
        self.interval_var: tk.DoubleVar = tk.DoubleVar(None, self.master.data.min_wait_time)
        tk.Entry(self.top_frame, textvariable= self.interval_var, font= self.font).grid(row= 5, column= 1)
        
        for child in self.top_frame.winfo_children():
            child.grid_configure(padx= 10, pady= 5)
        
        self.top_frame.pack(side= tk.TOP, anchor= tk.CENTER)
 
    def add_option(self):
        self.options_list.append(self.name_var.get())
        self.option_menu['menu'].add_command(label= self.name_var.get(), command= tk._setit(self.options_var, self.name_var.get()))
        self.options_var.set(self.name_var.get())
        self.name_var.set('')

    def remove_selected_option(self):
        try:
            self.options_list.remove(self.options_var.get())
        except ValueError: # trying to remove from an empty option menu
            return
        index = self.option_menu['menu'].index(self.options_var.get())
        self.option_menu['menu'].delete(index)
        self.options_var.set(self.option_menu['menu'].entrycget(0,"label"))

    def set_image(self):
        file_path: str = filedialog.askopenfilename(title= self.master.title())
        for ending in ["gif", "png", "tiff", "webp", "ppm", "jpeg", "jpg", "bmp"]:
            if file_path.endswith(ending):
                break
        else:
            return
        
        self.master.data.message = Image.open(file_path)           
        self.message_var.set('')