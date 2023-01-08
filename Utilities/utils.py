import inspect

class Utils:

    def get_test_case_title(self):
        return inspect.currentframe().f_back.f_code.co_name