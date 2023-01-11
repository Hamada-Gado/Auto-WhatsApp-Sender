import shelve
import sys
from pathlib import Path
from typing import Any

from PIL import Image

class Data:
    # constants
    SAVE_FILE_PATH  : Path  = Path(sys.path[0]) / "App Data" / "data"
    WHATSAPP_TITLE  : str   = "WhatsApp"
    WHATSAPP_URL    : str   = "https://web.whatsapp.com/"
    WHATSAPP_PATH   : Path  = Path("WhatsApp.exe")
    NAMES           : list  = list()
    
    # Default data
    DEFAULT: dict[str, Any] = {
        'whatsApp_path' : WHATSAPP_PATH,
        'names'         : NAMES,
        'message'       : "This message was send by an auto sender",
        'online'        : True,
        'min_wait_time' : 5,
        'interval'      : 0.1
    }

    def __init__(self) -> None:
        self.whatsApp_path: Path
        self.names: list[str]
        self.message: str | Image.Image
        self.online: bool
        self.min_wait_time: float
        self.interval: float = 0.1
        self.load()
        
    def save(self) -> None:
        if not Data.SAVE_FILE_PATH.parent.exists():
            Data.SAVE_FILE_PATH.parent.mkdir()
        
        with shelve.open(Data.SAVE_FILE_PATH.as_posix()) as shelf_file:
            shelf_file["data"] = self
    
    def load(self) -> None:
        Data.SAVE_FILE_PATH.parent.mkdir(exist_ok= True)
        
        with shelve.open(Data.SAVE_FILE_PATH.as_posix()) as shelf_file:
            try:
                other: Data = shelf_file["data"]
                self.__dict__.update(other.__dict__)
            except KeyError:
                self.__dict__.update(Data.DEFAULT)
            
    def load_default(self) -> None:
        self.__dict__.update(Data.DEFAULT)
            
    def __str__(self) -> str:
        return f"{self.__dict__}"
                