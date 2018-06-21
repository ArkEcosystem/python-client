
class ArkException(Exception):
    pass


class ArkParameterException(ArkException):
    pass


class ArkHTTPException(ArkException):

    def __init__(self, *args, **kwargs):
        self.response = kwargs.pop('response', None)
        super().__init__(*args, **kwargs)
