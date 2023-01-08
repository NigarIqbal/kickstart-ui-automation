import logging
import os
import datetime

class CustomLogger:

    @staticmethod
    def generate_log():
        logger = logging.getLogger()

        log_dir = f'{os.getcwd()}\\Logs'

        file_name = f'AutomationLog-{datetime.datetime.now().strftime("%Y-%m-%d_%I%M%S %p")}'
        log_file = os.path.join(log_dir, f'{file_name}.log')
        file_handler = logging.FileHandler(log_file, mode = 'w')
        log_formatter = logging.Formatter(
            "%(asctime)s :%(levelname)s : {%(filename)s:%(module)s:%(lineno)d} %(levelname)s :%(message)s")
        file_handler.setFormatter(log_formatter)

        console_log = logging.StreamHandler()
        console_log.setLevel(logging.DEBUG)
        console_log.setFormatter(log_formatter)

        logger.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)
        logger.addHandler(console_log)

        return logger


