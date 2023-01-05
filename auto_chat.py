import subprocess, pyautogui as pag

WHATS_APP_PATH              = r'C:\"Program Files"\WindowsApps\5319275A.WhatsAppDesktop_2.2248.9.0_x64__cv1g1gvanyjgm\WhatsApp.exe'
WHATS_APP_LOGO_IMAGE_PATH   = "WhatsApp Logo.png" 

def open_app():
    subprocess.run(f'start "" {WHATS_APP_PATH}', shell = True)
    pag.locateOnScreen(image= WHATS_APP_LOGO_IMAGE_PATH, minSearchTime= 5) # make sure that the window opened before maximizing it to not throw an error
    pag.getWindowsWithTitle("WhatsApp")[0].maximize() # type: ignore
    
def main():
   open_app() 
    
if __name__ == "__main__":
    main()