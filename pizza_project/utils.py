import logging
import os


def create_logger_module(module_name):
    """
    Create logger module
    :param module_name:
    :return:
    """
    logger_format = '%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
    logging.basicConfig(format=logger_format, datefmt='%d-%m-%Y:%H:%M:%S',
                        level=os.environ.get('LOGGING_LEVEL', logging.INFO))
    logger = logging.getLogger(module_name)
    return logger


def get_logger():
    """
    get logger
    :return:
    """
    logger = logging.getLogger("pizza-order-system")
    logger.setLevel(os.environ.get("LOGGING_LEVEL", logging.INFO))
    ch_handler = logging.StreamHandler()
    ch_handler.setLevel(os.environ.get("LOGGING_LEVEL", logging.INFO))
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch_handler.setFormatter(formatter)
    logger.addHandler(ch_handler)
    return logger


LOGGER = get_logger()