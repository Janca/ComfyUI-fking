import abc
import time


class FkBasicNode:

    CATEGORY = "fking"
    FUNCTION = "execute"

    OUTPUT_NODE = False

    @abc.abstractmethod
    def execute(self, *args):
        raise NotImplementedError()
