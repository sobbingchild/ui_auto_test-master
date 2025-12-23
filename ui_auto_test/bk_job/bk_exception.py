
class BluekingException(Exception):
    def __init__(self,msg=None):
        self.msg = msg
    def __str__(self):
        excetion_msg = 'Messgae: {}'.format(self.msg)
        return excetion_msg

class LoginError(BluekingException):
    " check Login product_page success or false "
    pass

class ApiError(BluekingException):
    " check api success or false "
    pass