from loguru import logger
import sys

logger.remove()  # Remove the default handler
logger.add(sys.stdout, level="DEBUG", format="{time} {level} {message}", backtrace=True, diagnose=True)
logger.add("logs/debug.log", level="DEBUG", rotation="10 MB", compression="zip")
logger.add("logs/error.log", level="ERROR", rotation="10 MB", compression="zip")

def get_logger():
    return logger
