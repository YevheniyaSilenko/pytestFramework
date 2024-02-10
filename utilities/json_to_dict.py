class DictToClass:
    def __init__(self, **kwargs):
        self.url = None
        self.__dict__.update(**kwargs)