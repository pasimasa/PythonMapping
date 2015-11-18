import logging
import datetime

VERSION = "1.0"

def setup_logger(folder_name):
    """
    Create logger object for writing into log file and output to screen. 
    Creates new log for each day (good for scheduled tasks)
    """
    logger = logging.getLogger(VERSION)
    logger.setLevel(logging.DEBUG)
    now = datetime.datetime.now()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Output to log file
    log_file = os.path.join(folder_name, "ScriptLog_%s_%s_%s.log" % (now.day, now.month, now.year))
    handler = logging.FileHandler(log_file, "a", encoding=None, delay="true")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    # Output to screen
    stdout_handler = logging.StreamHandler()
    stdout_handler.setFormatter(formatter)
    logger.addHandler(stdout_handler)

    return logger

# Create logger, put logfile in \logs subfolder
script_dir = os.path.dirname(os.path.realpath(__file__)
log_folder = os.path.join(script_dir, "logs")
logger = setup_logger(log_folder)

def main():

    logger.info("some info messages")
    logger.warning("this is warning of some issue")
    logger.error("something is wrong")

if __name__ == '__main__':
    main()

    # Cleanup
    logger.handlers= []

