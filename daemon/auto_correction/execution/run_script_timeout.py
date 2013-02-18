"""

@author: anibal

"""
from threading import Timer

class ProcessTimeout:
    """
    Handler of the timer for setting a timeout to the automatic correction process
    """


    def __init__(self, process, timeout):
        self.process = process
        self.timeout = timeout
        self.ran = False
        self.timer = Timer(self.timeout, self.kill_proc)
    
    def kill_proc(self):
        self.process.kill()
        self.ran = True
    
    def start_timer(self):
        self.timer.start()
    
    def cancel_timer(self):
        self.timer.cancel()
