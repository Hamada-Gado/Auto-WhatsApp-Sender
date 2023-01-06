import subprocess, time, pyautogui as pag
from pygetwindow import Window
from pathlib import Path

WHATSAPP_PATH   : Path  = Path('C:/Program Files/WindowsApps/5319275A.WhatsAppDesktop_2.2248.9.0_x64__cv1g1gvanyjgm/WhatsApp.exe')
WHATSAPP_WINDOW : Window

def open_app(minSearchTime= 5) -> None:
    global WHATSAPP_WINDOW
    
    subprocess.run(['start', "", WHATSAPP_PATH], shell = True)
    start_time = time.time()

    while time.time() - start_time < minSearchTime:
        try:
            WHATSAPP_WINDOW = pag.getWindowsWithTitle("WhatsApp")[0] # type: ignore
        except IndexError:
            continue
        break
    try:
        assert(WHATSAPP_WINDOW)
    except NameError:
        return # TODO raise error if can't open the app
    else:
        WHATSAPP_WINDOW.activate()
        WHATSAPP_WINDOW.maximize()
    
def main():
   open_app() 
    
if __name__ == "__main__":
    main()