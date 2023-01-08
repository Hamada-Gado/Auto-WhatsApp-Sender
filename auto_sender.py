import subprocess
import time
from io import BytesIO
from pathlib import Path
from tkinter import messagebox

import pyautogui as pag
import pygetwindow as pgw
import pyperclip
import webbrowser
import win32clipboard  # type: ignore
from PIL import Image

from debug.test import *
from exceptions import *

class Auto_Sender():
    # TODO make it possible to send more than one text message or photo
    
    WHATSAPP_TITLE  : str   = "WhatsApp"
    WHATSAPP_URL    : str   = "https://web.whatsapp.com/"
    OPINING_METHOD  : bool  = True
    
    def __init__(self, whatsApp_path: Path = PATH) -> None:
        self.whatsApp_path = whatsApp_path
        self.whatsApp_window : pgw.Window
                
    def set_message(self, message: str | Image.Image):
        if isinstance(message, str):
            self._send_text_to_clipboard(message)
            return
        
        if isinstance(message, Image.Image):
            self._send_image_to_clipboard(message)
            return

    def _send_image_to_clipboard(self, image: Image.Image):
        output = BytesIO()
        image.convert('RGB').save(output, 'BMP')
        data = output.getvalue()[14:]
        output.close()

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()
        
    def _send_text_to_clipboard(self, message: str):
        pyperclip.copy(message)

    def open_app_offline(self, minSearchTime= 5) -> None:
        subprocess.run(['start', "", self.whatsApp_path], shell = True).check_returncode()

        start_time = time.time()
    
        while True:
            try:
                for window in pgw.getWindowsWithTitle(Auto_Sender.WHATSAPP_TITLE):
                    if window.title == Auto_Sender.WHATSAPP_TITLE:
                        self.whatsApp_window = window
                        break
                else:
                    raise WindowNotFoundException

            except WindowNotFoundException:
                if time.time() - start_time > minSearchTime:
                    raise WindowNotFoundException
                continue
            break
        
        while not self.whatsApp_window.isActive: # wait for the window to be active
            pass
        
        self.whatsApp_window.maximize()
        time.sleep(minSearchTime) # wait to make sure the application is ready for shortcuts
        
    def open_app_online(self) -> None:
        if not webbrowser.open_new(Auto_Sender.WHATSAPP_URL):
            raise WindowNotFoundException
        
        time.sleep(5)
        pag.press("f11")
        
    def send(self,*args, **kwargs):
        if self.OPINING_METHOD:
            self._send_offline(*args, **kwargs)
        else:
            self._send_online(*args, **kwargs)

    def _send_offline(self, name: str, outer_interval: float = 0.5, internal_interval: float = 0.1) -> None:
        pag.hotkey("ctrl", "1", interval= internal_interval)
        pag.hotkey("ctrl", "f", interval= internal_interval)
        pag.hotkey("ctrl", "a", interval= internal_interval)
        pag.press("backspace", interval= internal_interval)
        time.sleep(outer_interval)
        
        pag.typewrite(name, interval= internal_interval)
        time.sleep(outer_interval)
        
        pag.hotkey("ctrl", "1", interval= internal_interval)
        time.sleep(outer_interval)
        
        pag.hotkey("ctrl", "v", interval= internal_interval)
        pag.press("enter")
        
    def _send_online(self, name: str, outer_interval: float = 1.5, internal_interval: float = 0.1):
        pag.hotkey("alt", "k", interval= internal_interval)
        
        #// pag.hotkey("ctrl", "alt", "/", interval= internal_interval)
        #// pag.hotkey("ctrl", "alt", "/", interval= internal_interval)

        pag.hotkey("ctrl", "a", interval= internal_interval)
        pag.press("backspace", interval= internal_interval)
        time.sleep(outer_interval)
        
        pag.typewrite(name, interval= internal_interval)
        time.sleep(outer_interval)
        
        pag.press("enter", interval= internal_interval)
        time.sleep(outer_interval)
        
        pag.hotkey("ctrl", "v", interval= internal_interval)
        pag.press("enter")
        
    def send_all(self):
        for name in NAMES:
            self.send(name)

    def run(self) -> None:
        try:
            self.open_app_online() 
        except subprocess.CalledProcessError: # the os handles it
            return
        except WindowNotFoundException as e:
            messagebox.showerror(title= "Window not found", message= str(e))
            return

        self.set_message(TEXT)
        self.send_all()