import logging  # Imported teh logging package

logging.basicConfig(level=logging.INFO,filename="log_file.log",filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s") 
# here we are using the "bnasicConfig" of logging to set level of logging here we've set it to logging.debug so that we get all the log msgs right from debug to 
# critical (all 5 levels) and filename is "log_file.log" where teh logs will be saved and filemode is 'w' which is 'write' mode and overwrutes new stuff it file
# already exists and format is for formatting the output into a more human readable form like "asctime" is giving the datetime of the log , then levelname is there
# and lastly there is teh message

x = 7

# These are the 5 logging levels that we can log & by default the "warning", "error", "critical" log levels are printed of saved to afile that we specify
logging.debug("debugging")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

logging.info(f"The value of x is {x}")  # thsi example of how you can log the values of a variable

# Logging the exceptions    
try:
    1 / 0
except ZeroDivisionError as e:
    logging.exception("Zero Division error occured")


# Custom logger
logger = logging.getLogger(__name__) # made a custom logger name "logger" via getlogger and passed __name__ to get the name 

handler = logging.FileHandler("Custom_logger.log") # without adding the handler the custom logger logs would have been overwritter in our previous "log_file.log" file
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info("Testing the Custom Logger")