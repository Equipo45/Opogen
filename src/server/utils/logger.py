import logging
import os
from datetime import datetime


def setup_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    date_str = datetime.now().strftime("%Y-%m-%d")
    log_file = f"logs/logsfile_manipulation_{date_str}.log"

    if not os.path.exists(log_file):
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger


logger = setup_logger()
