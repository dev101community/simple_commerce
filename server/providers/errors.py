class APIException(Exception):
    def __init__(self, code, message):
        super().__init__()
        self.code = code
        self.description = message

class DataNotFoundException(APIException):
    """Custom exception when resource is not found."""
    def __init__(self, message):
        super().__init__(500, message)
