import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

file_handler = logging.FileHandler("errors.log", encoding="utf-8")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
