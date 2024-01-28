import logging
import os
import datetime

class CustomLogger:

    @staticmethod
    def generate_log():
        logger = logging.getLogger()

        # Set the logger's level to DEBUG
        logger.setLevel(logging.DEBUG)

        log_dir = f'{os.getcwd()}\\Logs'

        file_name = f'AutomationLog-{datetime.datetime.now().strftime("%Y-%m-%d_%I%M%S %p")}'
        log_file = os.path.join(log_dir, f'{file_name}.log')

        # Create a file handler
        file_handler = logging.FileHandler(log_file, mode='w')
        log_formatter = logging.Formatter("%(asctime)s :%(levelname)s : {%(filename)s:%(module)s:%(lineno)d} %(levelname)s :%(message)s")
        file_handler.setFormatter(log_formatter)

        # Add the file handler to the logger
        logger.addHandler(file_handler)

        # Create a console handler
        console_log = logging.StreamHandler()
        console_log.setLevel(logging.INFO)  # Set the console handler's level to INFO
        console_log.setFormatter(log_formatter)

        # Add the console handler to the logger
        logger.addHandler(console_log)

        return logger