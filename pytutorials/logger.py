'''
Tutorials Logging Script:
   
* Used for logging debugging and error messages related to the tutorials pages 

'''

import os
import logging

PARENT_MODULE_NAME = __name__.split(".")[0]
BASE_DIR = os.path.dirname(__file__).replace(PARENT_MODULE_NAME,'')

''' To call from other modules use
from pytutorials.logger import TUTORIALS_LOG

TUTORIALS_LOG.info('Blah blah blah')
'''
TUTORIALS_LOG = logging.getLogger(__name__)
TUTORIALS_LOG.setLevel('DEBUG')
log_file = logging.FileHandler(BASE_DIR + '/tutorials.log')
TUTORIALS_LOG.addHandler(log_file)