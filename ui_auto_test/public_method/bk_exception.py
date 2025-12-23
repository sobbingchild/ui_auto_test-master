class BluekingException(Exception):
    def __init__(self, msg=None):
        self.msg = msg

    def __str__(self):
        exception_msg = 'Messgae: {}'.format(self.msg)
        return exception_msg


class LoginError(BluekingException):
    " check Login page success or false "
    pass


class ApiError(BluekingException):
    " check api success or false "
    pass


class ElementOperationError(BluekingException):
    " element operation success of false "
    pass

class ElementPathError(BluekingException):
    " element path position success of false "