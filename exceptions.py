class WindowNotFoundException(Exception):
    MESSAGE = \
    """\
    Error: Window not found

    Possible Reasons: Application might have taken very long
    time to start.
            
    Possible Solution: Run the program again without closing
    the targeted application or increase the minimum search
    time for the window.\
    """
    
    def __init__(self) -> None:
        super().__init__(WindowNotFoundException.MESSAGE)