from __future__ import annotations

from enum import Enum


class Side(Enum):
    NORTH = 1
    SOUTH = -1
    EAST = 2
    WEST = -2
    UP = 3
    DOWN = -3

    @staticmethod
    def opposite(opposite: Side) -> Side:
        """
        Returns the opposite side
        :type opposite: Side
        """
        return Side(-1 * opposite.value)
