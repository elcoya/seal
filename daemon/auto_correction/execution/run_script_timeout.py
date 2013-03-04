"""

@author: anibal

"""
from threading import Timer
from auto_correction.log.logger_manager import LoggerManager

class ProcessTimeout:
    """
    Handler of the timer for setting a timeout to the automatic correction process
    """


    def __init__(self, process, timeout):
        self.process = process
        self.timeout = timeout
        self.ran = False
        self.timer = Timer(self.timeout, self.kill_proc)
        self.logger = LoggerManager().get_new_logger("process timeout")
    
    def kill_proc(self):
        self.logger.debug("timer expired, killing process...")
        self.process.kill()
        self.logger.debug("process terminate invoked.")
        self.ran = True
    
    def start_timer(self):
        self.logger.debug("timer started")
        self.timer.start()
    
    def cancel_timer(self):
        self.logger.debug("timer cancelled")
        self.timer.cancel()
