
class BluekingException(Exception):
    def __init__(self,msg=None):
        self.msg = msg
    def __str__(self):
        excetion_msg = 'Messgae: {}'.format(self.msg)
        return excetion_msg

