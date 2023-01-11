import subprocess
import time
import webbrowser
from io import BytesIO

import pyautogui as pag
import pygetwindow as pgw
import pyperclip
import win32clipboard
from PIL import Image

from data import Data
from exceptions import *


class Auto_Sender():
    # TODO make it possible to send more than one text message or photo 
    
    def __init__(self, data: Data) -> None:
        self.data: Data = data
                
    def set_message(self, message: str | Image.Image) -> None:
        if isinstance(message, str):
            self._send_text_to_clipboard(message)
            return
        
        if isinstance(message, Image.Image):
            self._send_image_to_clipboard(message)
            return

    def _send_image_to_clipboard(self, image: Image.Image) -> None:
        output = BytesIO()
        image.convert('RGB').save(output, 'BMP')
        data = output.getvalue()[14:]
        output.close()

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()
        
    def _send_text_to_clipboard(self, message: str) -> None:
        pyperclip.copy(message)

    def open(self, minWaitTime: float = 5) -> None:
        if self.data.online:
            self._open_app_online(minWaitTime)
        else:
            self._open_app_offline(minWaitTime)

    def _open_app_offline(self, minWaitTime: float = 5) -> None:
        subprocess.run(['start', "", self.data.whatsApp_path], shell = True).check_returncode()
        
        whatsApp_window: pgw.Window | None = None
        start_time = time.time()
        
        while time.time() - start_time < minWaitTime:
            for window in pgw.getWindowsWithTitle(self.data.WHATSAPP_TITLE):
                if window.title == self.data.WHATSAPP_TITLE:
                    whatsApp_window = window
            
    
        if whatsApp_window is None:
            raise WindowNotFoundException  
            
        start_time = time.time()
        while not whatsApp_window.isActive: # wait for the window to be active
            if time.time() - start_time > minWaitTime:
                raise WindowNotFoundException

        whatsApp_window.maximize()
        time.sleep(minWaitTime) # wait to make sure the application is ready for shortcuts
    
    def _open_app_online(self, minWaitTime: float = 5) -> None:
        if not webbrowser.open_new(self.data.WHATSAPP_URL):
            raise WindowNotFoundException
        
        time.sleep(minWaitTime) # wait to make sure the application is ready for shortcuts 
        pag.press("f11")
        
    def send(self, *args, **kwargs) -> None:
        if self.data.online:
            self._send_online(*args, **kwargs)
        else:
            self._send_offline(*args, **kwargs)

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
        
        
    def _send_online(self, name: str, outer_interval: float = 1.5, internal_interval: float = 0.1) -> None:
        pag.hotkey("alt", "k", interval= internal_interval)

        pag.hotkey("ctrl", "a", interval= internal_interval)
        pag.press("backspace", interval= internal_interval)
        time.sleep(outer_interval)
        
        pag.typewrite(name, interval= internal_interval)
        time.sleep(outer_interval)
        
        pag.press("enter", interval= internal_interval)
        time.sleep(outer_interval)
        
        pag.hotkey("ctrl", "v", interval= internal_interval)
        pag.press("enter")
        
    def send_all(self, internal_interval: float = 0.1) -> None:
        for name in self.data.names:
            self.send(name, internal_interval= internal_interval)
            
    def check_data(self) -> None:
        if len(self.data.names) == 0:
            raise NamesNotFoundException
        if isinstance(self.data.message, str) and len(self.data.message) == 0:
            raise MessageNotFoundException
          
    def run(self) -> None: 
        self.check_data()   
        self.open(self.data.min_wait_time)
        self.set_message(self.data.message)
        self.send_all(self.data.interval)