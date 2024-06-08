import os
from .._config import config

__name__ = ""
__version__ = ""
__license__ = ""

class Conf(config):
    def __init__(self,name,**args):
        super().__init__(name=name,**args)
        default_set = [
            ["width",800],
            ["height",800],
            ["font","Meiryo UI"],
            ["dev_mode",0],
            ["Theme","default"],
        ]
        self.__version__ = __version__
        self.__name__ = __name__
        self.__license__ = __license__
        self.set_log()
        for ds in default_set:
            if self.get_data(ds[0])==0:
                self.set_data(ds[0],ds[1])

appconf = Conf(name=__name__)