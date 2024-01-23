import logging
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

anonymous_filter = lambda x: x.lower().count("я") >= 23

string = "яяяяяяяяяяяяяяяяяяяяяяяя, яяяяяяяяяяяяяяяя и яяяяяяяя тоже!"
logger.debug("string" + string)
logger.debug(logger.handlers)
stderr_handler = logging.StreamHandler()

stdout_handler = logging.StreamHandler(sys.stdout)

logger.addHandler(stderr_handler)
logger.addHandler(stdout_handler)
print(logger.handlers)

