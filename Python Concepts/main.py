import logging

# Set up the logging configuration
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s- %(name)s-%(levelname)s- %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


# # Example log messages from ROOT
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')


###  Creating own internal logger 
import helper
## check the helper.py


### file config method

import logging
import logging.config

logging.config.fileConfig('logging.conf')
logger = logging.getLogger("simpleExample")
logger.debug('this is a debug message')

#logging.config.DictConfig('logging.conf')
# also can dict config




### Troubleshooting 

import logging
try:
    a = [1, 2, 3]
    val = a[4]
except IndexError as e:
    logging.error(e) #ERROR:root:list index out of range
    logging.error(e, exc_info=True) # in details, line 42, val = a[4]


## When we dont know what error we have\
import logging
import traceback
try:
    a = [1, 2, 3]
    val = a[4]
except:
    logging.error("This error is %s", traceback.format_exc())
    #val = a[4], line 53, IndexError: list index out of range


### rotating file handler with backup , and size
import logging
from logging.handlers import RotatingFileHandler


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#roll over after 2kb, and keep backup logs app.log.1 app.log2. .. etc
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
    #create max 5 file with 2kb max size
logger.addHandler(handler)


for _ in range(10000):
    logger.info("hello, world")


### rotating file handler with Time
import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# 
handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)
logger.addHandler(handler)

for _ in range(6):
    logger.info('Hello, world!')
    time.sleep(5)