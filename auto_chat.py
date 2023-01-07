import subprocess, time, pygetwindow as pgw, pyautogui as pag
from pathlib import Path
from tkinter import messagebox
from Exceptions import *

WHATSAPP_PATH   : Path  = Path('C:/Program files/WindowsApps/5319275A.WhatsAppDesktop_2.2248.9.0_x64__cv1g1gvanyjgm/WhatsApp.exe')
WHATSAPP_TITLE  : str   = "WhatsApp"
WHATSAPP_WINDOW : pgw.Window

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
    
def main() -> int:
    try:
        open_app() 
    except subprocess.CalledProcessError:
        return 1
    except WindowNotFoundException as e:
        messagebox.showerror(title= "Window not found", message= str(e))
        return 2
    else:
        return 0
        
if __name__ == "__main__":
    main()