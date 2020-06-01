import json

class BillBot:
    
    # variables
    _Message = ''
    _service_list = []

    # Constructor for BillBot base class
    def __init__(self, message_header, service_list = []):
        self._Message = message_header
        self._service_list = service_list

    def print_message(self):         # virtual function declaration
        raise NotImplementedError
