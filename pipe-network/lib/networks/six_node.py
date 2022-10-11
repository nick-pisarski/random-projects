from __future__ import annotations

import logging
from os import path
from typing import Any, Dict, Optional

from lib.networks.side import Side

log = logging.getLogger(path.basename(__file__))


class SixNode:
    """A node with 6 pointers"""
    sides: Dict[Side, Optional[SixNode]] = {
        Side.NORTH: None,
        Side.SOUTH: None,
        Side.EAST: None,
        Side.WEST: None,
        Side.UP: None,
        Side.DOWN: None,
    }

    list_id: int = None,
    data: Optional[Any] = None

    def set_side(self, side: Side, new_node: SixNode) -> None:
        if self.sides[side] is None:
            raise Exception("Side occupied, please remove first.")
        self.sides[side] = new_node

    def get_side(self, side: Side) -> SixNode:
        return self.sides[side]

    def has_side(self, side: Side) -> bool:
        return self.sides[side] is not None

    def remove_side(self, side: Side) -> None:
        self.sides[side] = None


class SixNodeList:
    head: SixNode = None

    def append(self, end_node: SixNode, side: Side, new_node: SixNode) -> None:
        if self.head is None or self.head is end_node:
            self.head = new_node

        end_node.set_side(side, new_node)
        new_node.set_side(Side.opposite(side), new_node)
