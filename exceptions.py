class MyException(Exception):
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

class WindowNotFoundException(MyException):
    
    def __init__(self) -> None:
        message: str = \
        """\
        Error: Window not found

        Reasons: Application might have taken very long
        time to start or there is no internet connection if
        you are using online mode

        Solution: Run the program again without closing
        the WhatsApp application or increase the minimum search
        time for the window or check your internet connection if
        you are using online mode\
        """
    
        super().__init__(message)

class NamesNotFoundException(MyException):
   
    def __init__(self) -> None:
        message: str = \
        """\
        Error: Names not found
    
        Reasons: Did not save a list of names of at
        least one person to send
                
        Solution: Go to settings then names and add
        a minimum of one name
        """
   
        super().__init__(message)
        
class MessageNotFoundException(MyException):
    
    def __init__(self) -> None:
        message: str = \
        """\
        Error: Message not found

        Reasons: No text message or image is saved to send

        Solution: Go to settings then message and
        add a text or path to an image\
        """

        super().__init__(message)