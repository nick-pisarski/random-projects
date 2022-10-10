import logging
from os import path

log = logging.getLogger(path.basename(__file__))


class PipeInterface:
    pass


class PipeNode:
    pass


class PipeNetwork:
    """A class for managing a network"""

    def __init__(self) -> None:
        self.nodes: list[PipeNode] = []
        self.interfaces: list[PipeInterface] = []

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass
