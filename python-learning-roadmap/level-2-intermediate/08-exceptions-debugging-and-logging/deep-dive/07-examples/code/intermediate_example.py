import logging
logger = logging.getLogger(__name__)
try:
    total = 10 / 0
except ZeroDivisionError:
    logger.exception("Calculation failed")
