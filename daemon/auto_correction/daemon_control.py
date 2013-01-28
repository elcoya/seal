#!/usr/bin/python
import time
from datetime import datetime
from daemon.runner import DaemonRunner

from seal import settings #your project settings file
from django.core.management import setup_environ #environment setup function
from auto_correction.log.log import Log
import argparse
setup_environ(settings)

from auto_correction.automatic_correction_runner import AutomaticCorrectionRunner

class LoopRunner():
    
    LOOP_INTERVAL = 65
    
    def __init__(self):
        self.loop_interval = LoopRunner.LOOP_INTERVAL # in seconds
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/foo.pid'
        self.pidfile_timeout = 5
        self.automatic_correction_runner = AutomaticCorrectionRunner()
    
    def stall_loop(self, start_timestamp, finish_timestamp):
        delta = finish_timestamp - start_timestamp
        time_to_wait = self.loop_interval - delta.seconds # if the process took less than 30 seconds, we will wait
        if (time_to_wait > 0):
            time.sleep(time_to_wait)
        else:
            print("not sleeping... delta: " + str(delta))
        start_timestamp = datetime.today()
    
    def print_result(self, result):
        # TODO: pass to a log entry
        print str(datetime.today()) + " | " + str(result)
    
    def run(self):
        log = Log()
        log.info("Daemon's game loop started.")
        while True:
            start_timestamp = datetime.today()
            
            result = self.automatic_correction_runner.run()
            self.print_result(result)
            
            finish_timestamp = datetime.today()
            self.stall_loop(start_timestamp, finish_timestamp)

parser = argparse.ArgumentParser(description='Starts or stops the seal daemon.')
parser.add_argument('command', metavar='start/stop', 
                    help='the command that should be executed on the daemon')
args = parser.parse_args()

log = Log()
log.info("Daemon action recived: " + args.command)

loop_runner = LoopRunner()
daemon_runner = DaemonRunner(loop_runner) # runner.DaemonRunner(loop_runner)
daemon_runner.do_action()

if("start".__eq__(args.command.lower())):
    log.info("Daemon launched.")
else:
    log.info("Daemon stopped.")
