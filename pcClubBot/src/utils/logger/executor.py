import logging
<<<<<<< HEAD
=======
import os.path
>>>>>>> develop
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# logging.basicConfig(level=logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)


<<<<<<< HEAD
file_handler = RotatingFileHandler("latest.log", maxBytes=10*1024*1024, backupCount=3)
=======
file_handler = RotatingFileHandler(os.path.join(os.path.abspath(os.path.curdir), "latest.log"), maxBytes=10*1024*1024, backupCount=3)
>>>>>>> develop
file_handler.setFormatter(formatter)


logger.addHandler(console_handler)
logger.addHandler(file_handler)