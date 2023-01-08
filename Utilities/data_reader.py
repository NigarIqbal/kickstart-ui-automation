import json
import os
from Utilities.custom_logger import CustomLogger

class DataReader:

    log = CustomLogger.generate_log()

    def __init__(self, data_file, root_dir=os.getcwd()):
        try:
            file_path = f'{root_dir}\TestData\{data_file}.json'
            self.log.info(f'Data file {data_file} path is: {file_path}')
            is_file = os.path.isfile(file_path)
            if is_file == True:
                with open(file_path, 'r') as infile:
                    self.data = json.load(infile)
            else:
                self.log.info(f'File {data_file} does not exist')
        except Exception as e:
            self.log.exception(e)

    def get_base_url(self):
        return self.data['defaults']['url']

    def get_test_case_data(self, test_case):
        for obj in self.data['test_cases']:
            if obj['test_title'] == test_case:
                self.test_data = obj
                return self.test_data
            else:
                self.log.info(f'{test_case} not found in {self.data}')




