'''
Created on 27/01/2013

@author: anibal
'''
import logging

class Log:
    
    LOGGER = None
    LOGGER_NAME = " SEAL DAEMON"
    
    # FIXME: This should be in a configuration file or otherwise not hardcoded
    logfile = "seal-daemon.log"
    
    def __init__(self):
        if(Log.LOGGER is None):
            logging.basicConfig(filename=self.logfile, format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG, 
                                datefmt='%Y-%m-%d %H:%M:%S')
            Log.LOGGER = logging.getLogger(Log.LOGGER_NAME)
    
    def critical(self, message):
        Log.LOGGER.critical(message)
    
    def error(self, message):
        Log.LOGGER.error(message)
    
    def warning(self, message):
        Log.LOGGER.warning(message)
    
    def info(self, message):
        Log.LOGGER.info(message)
    
    def debug(self, message):
        Log.LOGGER.debug(message)
    
