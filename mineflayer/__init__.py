from .bot import Bot
from ._types import *
import logging as logging

logging.basicConfig(
    format="[%(asctime)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO
)