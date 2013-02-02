'''
Created on 27/01/2013

@author: anibal
'''
import logging
from auto_correction.utils import managepath

class LoggerManager:
    
    LOGGER = None
    LOGGER_FH = None
    
    LOGGER_NAME = "SEAL DAEMON"
    
    # FIXME: This should be in a configuration file or otherwise not hardcoded
    LOGFILE = managepath.get_instance().get_log_path() + "seal-daemon.log"
    LOG_LEVEL = logging.DEBUG
    
    def getLogger(self, logname=None):
        if(LoggerManager.LOGGER is None):
            # create logger with 'spam_application'
            logger = logging.getLogger(logname)
            logger.setLevel(logging.DEBUG)
            # create file handler which logs the messages
            fh = logging.FileHandler(LoggerManager.LOGFILE)
            fh.setLevel(LoggerManager.LOG_LEVEL)
            LoggerManager.LOGGER_FH = fh
            # create formatter and add it to the handler
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
            fh.setFormatter(formatter)
            # add the handler to the logger
            logger.addHandler(fh)
#            logging.basicConfig(filename=self.LOGFILE, format='%(asctime)s - %(name)s - %(levelname)s: %(message)s', level=logging.DEBUG,
#                                datefmt='%Y-%m-%d %H:%M:%S', )
            LoggerManager.LOGGER = logger
        return LoggerManager.LOGGER
    
    def get_file_handler(self):
        return LoggerManager.LOGGER_FH
    
    def get_new_logger(self, logname=None):
        # create logger with 'spam_application'
        if(logname):
            logger = logging.getLogger(logname)
        else:
            logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        # create file handler which logs the messages
        if (LoggerManager.LOGGER_FH is None):
            fh = logging.FileHandler(LoggerManager.LOGFILE)
            fh.setLevel(LoggerManager.LOG_LEVEL)
            LoggerManager.LOGGER_FH = fh
            # create formatter and add it to the handler
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
            fh.setFormatter(formatter)
            # add the handler to the logger
            logger.addHandler(fh)
        else:
            fh = LoggerManager.LOGGER_FH
        return logger
