class FileNotFoundException(Exception):
    
    def __init__(self, message: str) -> None:
        message = \
        f"""\
        Error: {message}

        Reasons: Application might have taken very long
        time to start

        Solution: Run the program again without closing
        the targeted application or increase the minimum search
        time for the window\
        """

        super().__init__(message)

class WindowNotFoundException(Exception):
    
    def __init__(self) -> None:
        message: str = \
        """\
        Error: Window not found

        Reasons: Application might have taken very long
        time to start

        Solution: Run the program again without closing
        the targeted application or increase the minimum search
        time for the window\
        """
    
        super().__init__(message)

class NamesNotFoundException(Exception):
   
    def __init__(self) -> None:
        message: str = \
        """\
        Error: Names not found
    
        Reasons: Did not save a list of names of at
        least one person to send
                
        Solution: Go to save variables then names and add
        a minimum of one name
        """
   
        super().__init__(message)
        
class MessageNotFoundException(Exception):
    
    def __init__(self) -> None:
        message: str = \
        """\
        Error: Message not found

        Reasons: No text message or image is saved to send

        Solution: Go to save variables then message and
        add a text or path to an image\
        """

        super().__init__(message)