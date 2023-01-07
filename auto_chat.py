import subprocess
import time
from pathlib import Path
from tkinter import messagebox
from typing import Generator

import pyautogui as pag
import pygetwindow as pgw

from Exceptions import *

WHATSAPP_PATH   : Path  = Path('C:/Program files/WindowsApps/5319275A.WhatsAppDesktop_2.2248.9.0_x64__cv1g1gvanyjgm/WhatsApp.exe')
WHATSAPP_TITLE  : str   = "WhatsApp"
WHATSAPP_WINDOW : pgw.Window
NAMES : list[str] = ["Ahmed Hisham", "Yousef Yasser", "Sawy"]
MESSAGE : str = "bagarb 7aga 3ady dagahl el resala de"

def open_app(minSearchTime= 5) -> None:
    global WHATSAPP_WINDOW
    
    try:
        subprocess.run(['start', "", WHATSAPP_PATH], shell = True).check_returncode()
    except subprocess.CalledProcessError:
        return
     
    start_time = time.time()
  
    while True:
        try:
            for window in pgw.getWindowsWithTitle(WHATSAPP_TITLE):
                if window.title == WHATSAPP_TITLE:
                    WHATSAPP_WINDOW = window
                    break
            else:
                raise WindowNotFoundException
            
        except WindowNotFoundException:
            if time.time() - start_time > minSearchTime:
                raise WindowNotFoundException
            continue
        break
    
    while not WHATSAPP_WINDOW.isActive: # wait for the window to be active
        pass
    
    WHATSAPP_WINDOW.maximize()
    time.sleep(minSearchTime) # wait to make sure the application is ready for shortcuts

def send(name: str, message: str, outer_interval= 0.5, internal_interval: float = 0.1) -> None:
    def instructions() -> Generator[None, None, None]:
        yield pag.hotkey("ctrl", "a", interval= internal_interval)
        yield pag.press("backspace", interval= internal_interval)
        yield pag.hotkey("ctrl", "f", interval= internal_interval)
        yield pag.typewrite(name, interval= internal_interval)
        yield pag.hotkey("ctrl", "1", interval= internal_interval)
        yield pag.typewrite(message, interval= internal_interval)
        yield pag.press("enter")
        
    for instruction in instructions():
        time.sleep(outer_interval)
    
def send_all():
    pag.hotkey("ctrl", "1")
    for name in NAMES:
        send(name, MESSAGE)
    
def main() -> None:
    try:
        open_app() 
    except subprocess.CalledProcessError: # the os handles it
        return
    except WindowNotFoundException as e:
        messagebox.showerror(title= "Window not found", message= str(e))
        return
        
    send_all()
        
if __name__ == "__main__":
    main()