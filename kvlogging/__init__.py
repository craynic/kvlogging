from .formatter import JsonFormatter, StreamFormatter
from .logger import Logger


def getLogger(name):
    return Logger(name)
