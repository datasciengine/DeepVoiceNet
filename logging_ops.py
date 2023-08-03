from datetime import datetime
from loguru import logger
import sys


class GeneralLogger:
    def __init__(self, module_name="Voice"):
        now_ts = datetime.now().strftime("%Y-%m-%d")
        fmt = "{time:YYYY-MM-DD HH:mm:ss} | {level} | {name} - {message}"
        logger.remove()  # All configured handlers are removed
        logger.add(f"../Volume/{module_name}_{now_ts}.log", level="TRACE", format=fmt)
        logger.add(sys.stderr, format=fmt)
        self.logger = logger
