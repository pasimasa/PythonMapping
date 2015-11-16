import logging, datetime

VERSION = "1.0"

def SetupLogger():
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
    stdOutHandler = logging.StreamHandler()
    stdOutHandler.setFormatter(formatter)
    logger.addHandler(stdOutHandler)

    return logger

# Create logger
logger = SetupLogger()

def main():

    logger.info("some info messages")
    logger.warning("this is warning of some issue")
    logger.error("something is wrong")

if __name__ == '__main__':
    main()

    # Cleanup
    logger.handlers= []

