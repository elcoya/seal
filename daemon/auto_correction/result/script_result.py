
class ScriptResult:
    """
    
    Container for automatic_correction running results. This class is going to be visited
    and the results published depending on who the visitor is.
    
    """

    def __init__(self):
        self.automatic_correction = None
        self.exit_value = 0
        self.captured_stdout = ""
    
    def accept(self, visitor):
        visitor.visit(self)
