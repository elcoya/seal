import ConfigParser
import sys
config = ConfigParser.ConfigParser()
config.readfp(open('../conf/local.cfg'))
sys.path.append(config.get("Path", "path.project.web"))      # Required to use the app model
sys.path.append(config.get("Path", "path.project.daemon"))      # Required to use the app model
sys.path.append(config.get("Path", "path.project.web") + "/seal/") # Fixes 'No module named model'

from seal import settings #your project settings file
from django.core.management import setup_environ #environment setup function

setup_environ(settings)

from daemon.autocheck_runner import AutocheckRunner
from datetime import datetime
import time

autocheck_runner = AutocheckRunner()
ref_timestamp = datetime.today()

while True:
    result = autocheck_runner.run()
    print "run check: results " + str(result)
    cur_timestamp = datetime.today()
    delta = cur_timestamp - ref_timestamp
    time_to_wait = 30 - delta.seconds # if the process took less than 30 seconds, we will wait
    if (time_to_wait > 0):
        time.sleep(time_to_wait)
    ref_timestamp = datetime.today()
