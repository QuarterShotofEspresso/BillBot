import Internet     # implement Internet
import Gas          # implement Gas

class BillBot:
    
    # variables
    _total
    _Message
    siteURL
    filepath
    site

    # Constructor for BillBot base class
    def __init__(self, msg, url, path, siteType):
        self.total = 0
        self.Message = msg
        self.siteURL = url
        self.filepath = path
        self.site = siteType


    # non virtual function collects data from file
    def collectMetadata(self):
        pass # TODO: Implement this function

    def printMessage(self):         # virtual function declaration
        raise NotImplementedError
