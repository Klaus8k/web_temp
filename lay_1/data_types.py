from loguru import logger
import pprint

a = 100
b = 1

logger.debug(bin(a))
logger.debug(a >> b)
logger.debug(bin(a >> b))