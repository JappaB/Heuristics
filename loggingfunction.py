import logging

# Logging: https://fangpenlin.com/posts/2012/08/26/good-logging-practice-in-python/
# or maybe http://www.patricksoftwareblog.com/python-logging-tutorial/
def setupLogger(fileHandler,
    loggingLevel,defaultLevel=logging.INFO,
    defaultFormat = ):

    """
    Setup logging configuratio

    -fileHandler indicates the file name to which will be logged

    -loggingLevel indicates how important the logg is, levels are (from unimportant to important):
    (DEBUG, INFO, WARNING, ERROR, CRITICAL).
    Default is set at INFO, to switch, give a logginglevel in the following manner:
    as second argument: logging.DEBUG for the DEBUG level.


    The default 

    """
    # formatter http://stackoverflow.com/questions/19765139/what-is-the-proper-way-to-do-logging-in-csv-file
    formatter = logging.Formatter('%(asctime)s,%(name)s,%(message)s')
    logger = logging.Getlogger(__name__)
    logger.setLevel(loggingLevel)
    fileHandler = fileHandler