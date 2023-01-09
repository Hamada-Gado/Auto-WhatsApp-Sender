import shelve
import sys
from enum import Enum
from pathlib import Path

from PIL import Image


class Data_Variables(Enum):
    whatsApp_path = "path"
    names = "names"
    message = "message"
    online = "online"
    

class Data:
    SAVE_FILE_PATH: Path = Path(sys.path[0]) / "App Data" / "data"

    def __init__(self) -> None:
        self.whatsApp_path: Path | None = None
        self.names: list[str] | None = None
        self.message: str | Image.Image | None = None
        self.online: bool = True
        self.load()
        
    def save(self) -> None:
        if not Data.SAVE_FILE_PATH.parent.exists:
            Data.SAVE_FILE_PATH.parent.mkdir()
        
        with shelve.open(Data.SAVE_FILE_PATH.as_posix()) as shelf_file:
            shelf_file["data"] = self
    
    def load(self) -> None:
        if not Data.SAVE_FILE_PATH.parent.exists:
            Data.SAVE_FILE_PATH.parent.mkdir()
        
        with shelve.open(Data.SAVE_FILE_PATH.as_posix()) as shelf_file:
            try:
                other: Data = shelf_file["data"]
                self.__dict__.update(other.__dict__)
            except KeyError:
                pass
            
    def __str__(self) -> str:
        return f"{self.__dict__}"
                