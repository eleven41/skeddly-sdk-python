
class SkeddlyException(Exception):
    def __init__(self, message):
        super(SkeddlyException, self).__init__(message)

class SkeddlyWebException(SkeddlyException):
    def __init__(self, message, errorCode):
        super(SkeddlyWebException, self).__init__(message)
        self.errorCode = errorCode

class ParameterValidationFailedException(SkeddlyWebException):
    def __init__(self, message, errorCode, modelState):
        super(ParameterValidationFailedException, self).__init__(errorCode, message)
        self.modelState = modelState
