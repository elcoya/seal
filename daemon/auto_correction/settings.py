'''
Created on 18/02/2013

@author: martin
'''

import os

#tools for working within jails#################################################
# set this to $JAIL_PATH when daemon runs within a jail
ROOT_FILES_PATH = None

# set to True overrides ROOT_FILES_PATH and uses regex to determine the 
# $JAIL_PATH to be chopped
SMART_PATH_ROUTING_ENABLED = False
################################################################################

#path customizables#############################################################
BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
WORKSPACE_PATH = BASE_PATH + "/workspace/"
AUTOMATIC_CORRECTION_TMP_PATH = WORKSPACE_PATH + "tmp_dir/"
LOG_PATH = WORKSPACE_PATH + "log/"
################################################################################

#rest information###############################################################
REST_BASE_URL = os.environ['REST_API_BASE_URL']
DAEMON_KEY = 'seal-daemon-authentication-key'
################################################################################

CORRECTION_ENABLED = False
MAIL_ENABLED = False


