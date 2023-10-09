import sys

def error_message_detail(error, error_detail: tuple):
    _, _, exc_tb = error_detail

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    error_message = f"Error occurred in Python script '{file_name}' at line {line_number}: {str(error)}"

    return error_message

class CustomException(Exception):
    def __init__(self, error, error_detail: tuple):
        """
        :param error: error message in string format
        :param error_detail: sys.exc_info() containing error details
        """
        super().__init__(str(error))

        self.error_message = error_message_detail(error, error_detail=error_detail)

    def __str__(self):
        return self.error_message
