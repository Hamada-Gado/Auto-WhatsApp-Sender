from auto_sender import Auto_Sender
from data import Data
from gui import Gui
class Main:
    
    def __init__(self) -> None:
        self.data: Data = Data() 
        self.gui: Gui = Gui(self, self.data)
        self.auto_sender: Auto_Sender = Auto_Sender(self.data)

    def main(self):
        self.auto_sender.run()

if __name__ == "__main__":
    Main().main()