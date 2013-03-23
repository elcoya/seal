'''
Created on 18/02/2013

@author: martin
'''

import os

#path customizables#############################################################
BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
WORKSPACE_PATH = BASE_PATH + "/workspace/"
AUTOMATIC_CORRECTION_TMP_PATH = WORKSPACE_PATH + "tmp_dir/"
LOG_PATH = WORKSPACE_PATH + "log/"
################################################################################

#rest information###############################################################
REST_BASE_URL = os.environ['REST_API_BASE_URL']
SECRET_KEY = ')q&!5_ig&s8h3w#l@2i#yn*=@6lhct+za(zpcb+%6p&@&^q-lv'
################################################################################




