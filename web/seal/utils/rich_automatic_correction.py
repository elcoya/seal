"""

@author: anibal

"""

class RichAutomaticCorrection:
    """
    Transfer bean to publish in the rest api for the daemon
    """


    def __init__(self, automatic_correction):
        """
        Constructor
        """
        self.pk = automatic_correction.pk
        self.delivery = automatic_correction.delivery
        self.captured_stdout = automatic_correction.captured_stdout
        self.exit_value = automatic_correction.exit_value
        self.status = automatic_correction.status
        self.delivery_file = automatic_correction.delivery.file
        self.script_file = automatic_correction.delivery.practice.get_script().file
    
