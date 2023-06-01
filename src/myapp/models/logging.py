import logging

# Configure the logger
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler()  # Output logs to console
        # Add more handlers if required (e.g., file handler)
    ]
)

# Create a logger instance
logger = logging.getLogger(__name__)


def log_debug(message):
    logger.debug(message)


def log_info(message):
    logger.info(message)


def log_warning(message):
    logger.warning(message)


def log_error(message):
    logger.error(message)


def log_critical(message):
    logger.critical(message)
