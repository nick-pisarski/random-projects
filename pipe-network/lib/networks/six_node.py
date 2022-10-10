from __future__ import annotations

import logging
from os import path
from typing import Any, Dict, Optional

from lib.networks.side import Side

log = logging.getLogger(path.basename(__file__))


class SixNode:
    """A node with 6 pointers"""
    """
    How do two nodes connect together?
    
    old_node.set_side(Side.XXXX, new_node)
    """
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

    def set_side(self, side: Side, value: SixNode) -> None:
        self.sides[side] = value

    def get_side(self, side: Side) -> SixNode:
        return self.sides[side]

    def has_side(self, side: Side) -> bool:
        return self.sides[side] is not None

    def remove_side(self, side: Side) -> None:
        self.sides[side] = None


class SixNodeList:
    head: SixNode = None

    def append(self, end_node: SixNode, new_node: SixNode) -> None:
        if self.head is None or self.head is end_node:
            self.head = new_node
