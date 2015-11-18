import logging
import datetime

VERSION = "1.0"

def setup_logger():
    """
    Create logger object for writing into log file and output to screen. 
    Creates new log for each day (good for scheduled tasks)
    """
    logger = logging.getLogger(VERSION)
    logger.setLevel(logging.DEBUG)
    now = datetime.datetime.now()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Output to log file
    handler = logging.FileHandler("ScriptLog_%s_%s_%s.log" % (now.day, now.month, now.year), "a", encoding=None, delay="true")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    # Output to screen
    stdout_handler = logging.StreamHandler()
    stdout_handler.setFormatter(formatter)
    logger.addHandler(stdout_handler)

    return logger

# Create logger
logger = setup_logger()

def main():

    logger.info("some info messages")
    logger.warning("this is warning of some issue")
    logger.error("something is wrong")

if __name__ == '__main__':
    main()

    # Cleanup
    logger.handlers= []

