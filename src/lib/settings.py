import json


class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls,*args,**kw):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kw)
        return cls._instance


def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getinstance


@singleton
class Settings(object):
    ROOT_DIR = None
    CONFIG = None
    # __metaclass__ = Singleton

    def init(self, root_dir):
        self.ROOT_DIR = root_dir
        
        with open('./config.json', 'r') as file:
            self.CONFIG = json.loads(file.read())
