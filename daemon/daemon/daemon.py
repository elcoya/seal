from seal import settings #your project settings file
from django.core.management import setup_environ #environment setup function

setup_environ(settings)

import sys
import os
import ConfigParser
config = ConfigParser.ConfigParser()
config.readfp(open(os.environ['PROJECT_PATH'] + 'daemon/conf/local.cfg'))
sys.path.append(config.get("Path", "path.project.web"))      # Required to use the app model
sys.path.append(config.get("Path", "path.project.daemon"))      # Required to use the app model
sys.path.append(config.get("Path", "path.project.web") + "seal/") # Fixes 'No module named model'

from daemon.autocheck_runner import AutocheckRunner
from datetime import datetime
import time

autocheck_runner = AutocheckRunner()
ref_timestamp = datetime.today()


import logging
l = logging.getLogger('django.db.backends')
l.setLevel(logging.DEBUG)
stream = open("/tmp/daemon.debug", "a")
l.addHandler(logging.StreamHandler(stream=stream))


while True:
    result = autocheck_runner.run()
    cur_timestamp = datetime.today()
    print str(cur_timestamp) + " | run check should not be running: results " + str(result)
    with open(config.get("Path", "path.daemon.log"), "a") as f:
        f.write(str(cur_timestamp) + " | run check: results " + str(result) + "\n")
    delta = cur_timestamp - ref_timestamp
    time_to_wait = 30 - delta.seconds # if the process took less than 30 seconds, we will wait
    if (time_to_wait > 0):
        time.sleep(time_to_wait)
    ref_timestamp = datetime.today()
