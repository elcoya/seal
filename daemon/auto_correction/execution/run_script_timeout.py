"""

@author: anibal

"""
from threading import Timer
from auto_correction.log.logger_manager import LoggerManager
import os
import psutil

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
    
    def killtree(self):    
        parent = psutil.Process(self.process.pid)
        for child in parent.get_children(recursive=True):
            self.logger.debug("killing process %d", child.pid)
            child.kill()
        self.logger.debug("killing process %d", parent.pid)
        parent.kill()
    
    def kill_proc(self):
        self.logger.debug("timer expired, killing process...")
        self.killtree()
        self.logger.debug("process terminate invoked.")
        self.ran = True
    
    def start_timer(self):
        self.logger.debug("timer started")
        self.timer.start()
    
    def cancel_timer(self):
        self.logger.debug("timer cancelled")
        self.timer.cancel()
